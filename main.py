from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core import AstrBotConfig
from .hitokoto_handler import get_hitokoto
from .baidu.beauty_handler import get_beauty_score
from .baidu.baidu_auth import init_baidu_credentials
from .wangzhe_handler import get_wangzhe_info

@register("XMZ", "祁筱欣", "啥都有的一个融合了乱七八糟功能的插件", "1.1.3")
class HitokotoPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        init_baidu_credentials(self.config)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
        logger.info("一言插件初始化完成")
    
    @filter.command("hitokoto")
    async def hitokoto_command(self, event: AstrMessageEvent):
        """获取一条一言。"""
        yield await get_hitokoto(event)
        
    @filter.command("测颜值")
    async def beauty_command(self, event: AstrMessageEvent):
        """发送人像图片获取颜值评分。"""
        # print(event.message_obj.raw_message) # 平台下发的原始消息在这里
        # print(event.message_obj.message) # AstrBot 解析出来的消息链内容
        yield await get_beauty_score(event)

    @filter.command("王者")
    async def wangzhe_command(self, event: AstrMessageEvent):
        """查询王者荣耀英雄资料。用法：王者 [英雄名称]"""
        message_segments = event.message_obj.message
        plain_text_parts = []
        if isinstance(message_segments, list):
            for segment in message_segments:
                if hasattr(segment, 'text'): # Check for .text attribute
                    plain_text_parts.append(str(segment.text)) # Convert to string
        full_text = "".join(plain_text_parts).strip()
        
        hero_name = ""
        
        command_keyword = "王者"
        # Check for "王者 HeroName"
        if full_text.lower().startswith(command_keyword.lower() + " "):
            hero_name = full_text[len(command_keyword) + 1:].strip()
        # Check for "/王者 HeroName"
        elif full_text.lower().startswith("/" + command_keyword.lower() + " "):
             hero_name = full_text[len(command_keyword) + 2:].strip()
        # If user types only "王者" or "/王者", hero_name remains "", which is handled by get_wangzhe_info

        yield await get_wangzhe_info(event, hero_name)

    @filter.command("xmz-help")
    async def help_command(self, event: AstrMessageEvent):
        """显示插件帮助信息。"""
        help_text = """
        === 一言插件帮助 ===
        命令列表:
        1. /hitokoto - 获取一条一言
        2. /测颜值 - 发送人像图片获取颜值评分
        3. /王者 [英雄名称] - 查询王者荣耀英雄资料 (例如：/王者 亚瑟)
        4. /xmz-help - 显示本帮助信息
        """
        yield event.plain_result(help_text)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        logger.info("一言插件已终止")
