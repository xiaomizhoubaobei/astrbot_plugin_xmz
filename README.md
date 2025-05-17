# 一言插件

一个为AstrBot设计的插件，提供一言语录和颜值评分功能。

## 功能详情
- 获取随机一言语录：从精选一言库中随机返回一条语录
- 通过图片分析颜值评分：基于百度AI开放平台的人脸识别API，分析人像照片并给出颜值评分

## 依赖要求
- Python 3.8+
- AstrBot框架
- 百度AI开放平台API Key（用于颜值评分功能）

## 功能
- 获取随机一言语录
- 通过图片分析颜值评分

## 命令列表
1. /hitokoto - 获取一条一言
2. /测颜值 - 发送人像图片获取颜值评分
3. /xmz-help - 显示帮助信息

## 安装
1. 将插件文件夹放入AstrBot的plugins目录
2. 重启AstrBot

## 配置
1. 百度API配置（颜值评分功能需要）
   - 前往[百度AI开放平台](https://ai.baidu.com/)申请API Key
   - 在插件配置文件中添加：
     ```
     [baidu]
     api_key = "your_api_key"
     secret_key = "your_secret_key"
     ```
2. 依赖安装
   - 运行 `pip install -r requirements.txt` 安装所需依赖

## 使用示例
```
/hitokoto
> 获取一条随机一言

/测颜值 [图片]
> 分析图片并返回颜值评分

/xmz-help
> 显示插件帮助信息
```

## 支持
如有问题，请参考[官方文档](https://astrbot.app)或联系开发者。
