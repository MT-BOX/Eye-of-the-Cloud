# Eye-of-the-Cloud
云之眼智能监控系统：
目前市场上监控产品很多，但大部分监控系统仍停留在传统监控的阶段。因
其缺乏对图像的智能分析，
普遍还处在一个只能“监”不能“控”的被动状态，
通常只是录制现场视频图像，用于事后作证，缺乏主动性和智能型，监控一旦装
好就只能监视一个角度的视野范围，实用性不强，不能做到全方位的监控，在之
后调用监控查找一些线索时，极大可能导致丢失关键线索。基于这种现状，我们
设计出“云之眼智能监控系统”。该系统通过对监控范围内人体的热量感应，激
活监控系统，
白天可直接打开并转动摄像头，对周围的人脸进行识别；在黑暗条
件下可与灯光系统相连，同时打开灯光系统，进行人脸识别。监控系统被激活后，
由
Raspberry Pi
控制转动舵机，
改变摄像头监控角度，
直至获取到清晰人的面
部特征并进行拍摄。拍摄后与数据库里的人脸进行比对，进而判断是否是陌生人，
该系统具备手机通信功能的
GSM
模块，能在第一时间将安全状况通过短信的形式
发送到用户的手机通知用户，用户在收到消息可及时赶到现场，避免重要财产的
丢失，
实现了监控系统的主动性和智能性。
