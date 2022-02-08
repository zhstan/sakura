# -*- encoding=utf8 -*-
__author__ = "maxiaojian"
from airtest.core.api import *
from poco.drivers.android.uiautomation import *
import requests
import json
import logging
import time
import urllib
import urllib3
urllib3.disable_warnings()

# def touch(img):
#     while exists(Template(r"tpl1619610906253.png", record_pos=(0.282, 0.806), resolution=(1080, 2340))):
#         sleep(1)
    
#     touch(img)
    
try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


def is_not_null_and_blank_str(content):
    """
    非空字符串
    :param content: 字符串
    :return: 非空 - True，空 - False
    """
    if content and content.strip():
        return True
    else:
        return False


class FeiShutalkChatbot(object):

    def __init__(self, webhook, secret=None, pc_slide=False, fail_notice=False):
        '''
        机器人初始化
        :param webhook: 飞书群自定义机器人webhook地址
        :param secret:  机器人安全设置页面勾选“加签”时需要传入的密钥
        :param pc_slide:  消息链接打开方式，默认False为浏览器打开，设置为True时为PC端侧边栏打开
        :param fail_notice:  消息发送失败提醒，默认为False不提醒，开发者可以根据返回的消息发送结果自行判断和处理
        '''
        super(FeiShutalkChatbot, self).__init__()
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.webhook = webhook
        self.secret = secret
        self.pc_slide = pc_slide
        self.fail_notice = fail_notice

    def send_text(self, msg, open_id=[]):
        """
        消息类型为text类型
        :param msg: 消息内容
        :return: 返回消息发送结果
        """
        data = {"msg_type": "text", "at": {}}
        if is_not_null_and_blank_str(msg):    # 传入msg非空
            data["content"] = {"text": msg}
        else:
            logging.error("text类型，消息内容不能为空！")
            raise ValueError("text类型，消息内容不能为空！")

        logging.debug('text类型：%s' % data)
        return self.post(data)

    def post(self, data):
        """
        发送消息（内容UTF-8编码）
        :param data: 消息数据（字典）
        :return: 返回消息发送结果
        """
        try:
            post_data = json.dumps(data)
            response = requests.post(self.webhook, headers=self.headers, data=post_data, verify=False)
        except requests.exceptions.HTTPError as exc:
            logging.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("消息发送失败, Request Exception!")
            raise
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                logging.error("服务器响应异常，状态码：%s，响应内容：%s" % (response.status_code, response.text))
                return {'errcode': 500, 'errmsg': '服务器响应异常'}
            else:
                logging.debug('发送结果：%s' % result)
                # 消息发送失败提醒（errcode 不为 0，表示消息发送异常），默认不提醒，开发者可以根据返回的消息发送结果自行判断和处理
                if self.fail_notice and result.get('errcode', True):
                    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                    error_data = {
                        "msgtype": "text",
                        "text": {
                            "content": "[注意-自动通知]飞书机器人消息发送失败，时间：%s，原因：%s，请及时跟进，谢谢!" % (
                                time_now, result['errmsg'] if result.get('errmsg', False) else '未知异常')
                        },
                        "at": {
                            "isAtAll": False
                        }
                    }
                    logging.error("消息发送失败，自动通知：%s" % error_data)
                    requests.post(self.webhook, headers=self.headers, data=json.dumps(error_data))
                return result
AndroidUiautomationPoco
ST.THRESHOLD = 0.7
ST.FIND_TIMEOUT = 30
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# # touch(Template(r"tpl1615531110556.png", record_pos=(-0.356, -0.302), resolution=(1080, 1920)))
poco("com.miui.home:id/workspace").offspring("妖D-STG2").offspring("com.miui.home:id/icon_icon").click()
sleep(10)
if exists(Template(r"tpl1605083586134.png", record_pos=(0.0, 0.531), resolution=(1079, 2340))):
    touch(Template(r"tpl1605083586134.png", record_pos=(0.0, 0.531), resolution=(1079, 2340)))
else:
    pass
touch(Template(r"tpl1605083605867.png", record_pos=(0.0, 0.624), resolution=(1079, 2340)))
sleep(8)
wait(Template(r"tpl1605083705959.png", record_pos=(0.003, 0.774), resolution=(1079, 2340)))
touch(Template(r"tpl1605083705959.png", record_pos=(0.003, 0.774), resolution=(1079, 2340)))
touch(Template(r"tpl1605083715193.png", record_pos=(0.187, 0.318), resolution=(1079, 2340)))
touch(Template(r"tpl1605083739443.png", record_pos=(-0.006, 0.267), resolution=(1079, 2340)))
touch(Template(r"tpl1605083753684.png", record_pos=(0.187, 0.261), resolution=(1079, 2340)))
sleep(3.0)
wait(Template(r"tpl1605088283818.png", record_pos=(0.189, 0.251), resolution=(1079, 2340)))
wait(Template(r"tpl1605089327854.png", record_pos=(0.007, 0.056), resolution=(1079, 2340)))
sleep(2)
touch(Template(r"tpl1605083768719.png", record_pos=(0.19, 0.255), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605083781009.png", record_pos=(0.379, 0.6), resolution=(1079, 2340)))
wait(Template(r"tpl1605089452200.png", record_pos=(0.016, 0.058), resolution=(1079, 2340)))
wait(Template(r"tpl1605089458323.png", record_pos=(-0.013, 0.138), resolution=(1079, 2340)))
wait(Template(r"tpl1605089462522.png", record_pos=(-0.154, 0.135), resolution=(1079, 2340)))

touch(Template(r"tpl1605083787858.png", record_pos=(-0.146, 0.138), resolution=(1079, 2340)))
wait(Template(r"tpl1605085191133.png", record_pos=(-0.152, 0.138), resolution=(1079, 2340)))
touch(Template(r"tpl1605083795303.png", record_pos=(0.193, 0.253), resolution=(1079, 2340)))
sleep(5.0)
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
wait(Template(r"tpl1605256744715.png", record_pos=(-0.002, 0.749), resolution=(1079, 2340)))
touch(Template(r"tpl1605083806127.png", record_pos=(0.379, 0.598), resolution=(1079, 2340)))
touch(Template(r"tpl1605083814792.png", record_pos=(-0.395, 0.366), resolution=(1079, 2340)))
touch(Template(r"tpl1605083822887.png", record_pos=(0.403, 0.23), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605083839429.png", record_pos=(-0.294, 0.81), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
wait(Template(r"tpl1605083966282.png", record_pos=(-0.39, 0.371), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605083832554.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1615532959572.png", record_pos=(0.39, 0.371), resolution=(1080, 1920)))
wait(Template(r"tpl1605688000531.png", record_pos=(0.18, 0.641), resolution=(1079, 2340)))
touch(Template(r"tpl1605084017390.png", record_pos=(0.187, 0.64), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
exists(Template(r"tpl1605258072595.png", record_pos=(0.379, 0.601), resolution=(1079, 2340)))
touch(Template(r"tpl1605083806127.png", record_pos=(0.379, 0.598), resolution=(1079, 2340)))
wait(Template(r"tpl1605084062545.png", record_pos=(-0.387, 0.826), resolution=(1079, 2340)))
wait(Template(r"tpl1605256948051.png", record_pos=(0.006, 0.541), resolution=(1079, 2340)))
touch(Template(r"tpl1605084069142.png", record_pos=(-0.397, 0.826), resolution=(1079, 2340)))
touch(Template(r"tpl1605084077024.png", record_pos=(0.199, 0.37), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605084035974.png", record_pos=(0.378, 0.599), resolution=(1079, 2340)))
touch(Template(r"tpl1605084069142.png", record_pos=(-0.397, 0.826), resolution=(1079, 2340)))
sleep(2)
touch(Template(r"tpl1605084108680.png", record_pos=(0.413, -0.408), resolution=(1079, 2340)))
sleep(2)
touch(Template(r"tpl1605084128030.png", record_pos=(-0.257, -0.222), resolution=(1079, 2340)))
touch(Template(r"tpl1605084138723.png", record_pos=(-0.397, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1615531436067.png", record_pos=(0.367, 0.552), resolution=(1080, 1920)))
touch(Template(r"tpl1605084153279.png", record_pos=(-0.396, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084160206.png", record_pos=(-0.33, 0.565), resolution=(1079, 2340)))
touch(Template(r"tpl1605084169187.png", record_pos=(-0.395, 0.361), resolution=(1079, 2340)))
touch(Template(r"tpl1605084175202.png", record_pos=(-0.326, 0.559), resolution=(1079, 2340)))
wait(Template(r"tpl1605084185486.png", record_pos=(-0.397, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084190109.png", record_pos=(-0.393, 0.373), resolution=(1079, 2340)))
touch(Template(r"tpl1605084196600.png", record_pos=(0.223, 0.683), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605084205474.png", record_pos=(0.375, 0.6), resolution=(1079, 2340)))
touch(Template(r"tpl1605084212917.png", record_pos=(-0.0, 0.247), resolution=(1079, 2340)))
touch(Template(r"tpl1605084219674.png", record_pos=(-0.396, 0.364), resolution=(1079, 2340)))
touch(Template(r"tpl1605084228366.png", record_pos=(-0.39, 0.371), resolution=(1079, 2340)))
touch(Template(r"tpl1605084233882.png", record_pos=(-0.388, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084239535.png", record_pos=(-0.392, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605084244567.png", record_pos=(-0.384, 0.371), resolution=(1079, 2340)))
touch(Template(r"tpl1605084250128.png", record_pos=(-0.392, 0.361), resolution=(1079, 2340)))
touch(Template(r"tpl1605084255787.png", record_pos=(-0.398, 0.368), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605084263207.png", record_pos=(0.376, 0.603), resolution=(1079, 2340)))
touch(Template(r"tpl1605084270042.png", record_pos=(-0.4, 0.363), resolution=(1079, 2340)))
touch(Template(r"tpl1605084275611.png", record_pos=(-0.405, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084280224.png", record_pos=(0.394, 0.404), resolution=(1079, 2340)))
sleep(3.0)
touch(Template(r"tpl1605084287313.png", record_pos=(0.186, 0.654), resolution=(1079, 2340)))
wait(Template(r"tpl1605084307895.png", record_pos=(-0.391, 0.364), resolution=(1079, 2340)))
touch(Template(r"tpl1605084311628.png", record_pos=(-0.399, 0.373), resolution=(1079, 2340)))
wait(Template(r"tpl1605085975726.png", record_pos=(-0.002, 0.732), resolution=(1079, 2340)))
wait(Template(r"tpl1605086083152.png", record_pos=(-0.003, 0.739), resolution=(1079, 2340)))
touch(Template(r"tpl1605086160711.png", record_pos=(-0.008, 0.758), resolution=(1079, 2340)))

touch(Template(r"tpl1605084325121.png", record_pos=(-0.395, -0.381), resolution=(1079, 2340)))
touch(Template(r"tpl1605084329925.png", record_pos=(-0.39, -0.388), resolution=(1079, 2340)))
touch(Template(r"tpl1605084334196.png", record_pos=(-0.4, 0.368), resolution=(1079, 2340)))
sleep(6.0)
wait(Template(r"tpl1605084353510.png", record_pos=(-0.391, 0.839), resolution=(1079, 2340)))
touch(Template(r"tpl1605084357500.png", record_pos=(-0.388, 0.834), resolution=(1079, 2340)))
touch(Template(r"tpl1605084362706.png", record_pos=(0.188, 0.368), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605084371616.png", record_pos=(0.376, 0.597), resolution=(1079, 2340)))
touch(Template(r"tpl1605084377727.png", record_pos=(-0.394, 0.37), resolution=(1079, 2340)))
touch(Template(r"tpl1605084382601.png", record_pos=(-0.392, 0.371), resolution=(1079, 2340)))
wait(Template(r"tpl1605084388844.png", record_pos=(-0.403, 0.361), resolution=(1079, 2340)))
touch(Template(r"tpl1605084392005.png", record_pos=(-0.395, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084397233.png", record_pos=(-0.398, 0.371), resolution=(1079, 2340)))
touch(Template(r"tpl1605084402117.png", record_pos=(-0.399, 0.371), resolution=(1079, 2340)))
touch(Template(r"tpl1605084407594.png", record_pos=(0.337, 0.444), resolution=(1079, 2340)))
wait(Template(r"tpl1605084419393.png", record_pos=(-0.405, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084423122.png", record_pos=(-0.398, 0.367), resolution=(1079, 2340)))
wait(Template(r"tpl1605257192113.png", record_pos=(-0.001, 0.417), resolution=(1079, 2340)))
wait(Template(r"tpl1605257199417.png", record_pos=(0.003, 0.144), resolution=(1079, 2340)))
touch(Template(r"tpl1605084431497.png", record_pos=(-0.347, 0.241), resolution=(1079, 2340)))
touch(Template(r"tpl1605084442998.png", record_pos=(-0.396, 0.362), resolution=(1079, 2340)))
sleep(3.0)
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605084449900.png", record_pos=(0.373, 0.605), resolution=(1079, 2340)))
touch(Template(r"tpl1605084455553.png", record_pos=(-0.388, 0.364), resolution=(1079, 2340)))
touch(Template(r"tpl1605084460639.png", record_pos=(-0.393, 0.361), resolution=(1079, 2340)))
touch(Template(r"tpl1605084466303.png", record_pos=(0.338, 0.45), resolution=(1079, 2340)))
sleep(3.0)
wait(Template(r"tpl1605084473177.png", record_pos=(-0.276, -0.312), resolution=(1079, 2340)))
touch(Template(r"tpl1605084476923.png", record_pos=(-0.281, -0.321), resolution=(1079, 2340)))
wait(Template(r"tpl1605084484104.png", record_pos=(0.35, -0.303), resolution=(1079, 2340)))
touch(Template(r"tpl1605084487568.png", record_pos=(0.355, -0.302), resolution=(1079, 2340)))
wait(Template(r"tpl1605084494177.png", record_pos=(0.31, -0.206), resolution=(1079, 2340)))
wait(Template(r"tpl1605086298027.png", record_pos=(-0.0, -0.237), resolution=(1079, 2340)))
wait(Template(r"tpl1605257296871.png", record_pos=(0.004, 0.054), resolution=(1079, 2340)))
touch(Template(r"tpl1605086510456.png", record_pos=(0.304, -0.224), resolution=(1079, 2340)))
wait(Template(r"tpl1605084506191.png", record_pos=(-0.396, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605084506191.png", record_pos=(-0.396, 0.367), resolution=(1079, 2340)))
wait(Template(r"tpl1605084512391.png", record_pos=(-0.394, 0.373), resolution=(1079, 2340)))
touch(Template(r"tpl1605084516168.png", record_pos=(-0.392, 0.37), resolution=(1079, 2340)))
touch(Template(r"tpl1605084520982.png", record_pos=(0.391, 0.413), resolution=(1079, 2340)))
wait(Template(r"tpl1605084534482.png", record_pos=(0.177, 0.662), resolution=(1079, 2340)))
touch(Template(r"tpl1605084538680.png", record_pos=(0.195, 0.664), resolution=(1079, 2340)))
wait(Template(r"tpl1605084707747.png", record_pos=(-0.391, 0.373), resolution=(1079, 2340)))
touch(Template(r"tpl1605084711911.png", record_pos=(-0.395, 0.373), resolution=(1079, 2340)))
touch(Template(r"tpl1605084716543.png", record_pos=(-0.399, 0.37), resolution=(1079, 2340)))
touch(Template(r"tpl1605084720737.png", record_pos=(-0.403, 0.369), resolution=(1079, 2340)))
touch(Template(r"tpl1605084725327.png", record_pos=(-0.385, 0.373), resolution=(1079, 2340)))
touch(Template(r"tpl1605084728901.png", record_pos=(-0.393, 0.376), resolution=(1079, 2340)))
wait(Template(r"tpl1605084749070.png", record_pos=(0.204, 0.37), resolution=(1079, 2340)))
wait(Template(r"tpl1605257404269.png", record_pos=(0.0, -0.082), resolution=(1079, 2340)))
touch(Template(r"tpl1605084753919.png", record_pos=(0.186, 0.378), resolution=(1079, 2340)))
wait(Template(r"tpl1605085433951.png", record_pos=(0.379, 0.602), resolution=(1079, 2340)))
touch(Template(r"tpl1605084760846.png", record_pos=(0.386, 0.601), resolution=(1079, 2340)))
wait(Template(r"tpl1605084768486.png", record_pos=(-0.383, 0.364), resolution=(1079, 2340)))
touch(Template(r"tpl1605084772345.png", record_pos=(-0.395, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084776312.png", record_pos=(-0.384, 0.37), resolution=(1079, 2340)))
touch(Template(r"tpl1605084780068.png", record_pos=(-0.406, 0.367), resolution=(1079, 2340)))
wait(Template(r"tpl1605084786344.png", record_pos=(0.0, 0.287), resolution=(1079, 2340)))
touch(Template(r"tpl1605084790679.png", record_pos=(-0.003, 0.285), resolution=(1079, 2340)))
wait(Template(r"tpl1605084798190.png", record_pos=(0.23, 0.601), resolution=(1079, 2340)))
touch(Template(r"tpl1605084802853.png", record_pos=(0.245, 0.613), resolution=(1079, 2340)))
wait(Template(r"tpl1605084808715.png", record_pos=(0.184, 0.29), resolution=(1079, 2340)))
touch(Template(r"tpl1605084813085.png", record_pos=(0.183, 0.295), resolution=(1079, 2340)))
wait(Template(r"tpl1605084854640.png", record_pos=(0.0, 0.807), resolution=(1079, 2340)))
while exists(Template(r"tpl1605084854640.png", record_pos=(0.0, 0.807), resolution=(1079, 2340))):
    touch(Template(r"tpl1605084854640.png", record_pos=(0.0, 0.807), resolution=(1079, 2340)))
    sleep(2)
    if exists(Template(r"tpl1611732637096.png", record_pos=(-0.005, 0.021), resolution=(1079, 2340))):     
        break
sleep(3)
touch(Template(r"tpl1605084934360.png", record_pos=(-0.384, 0.366), resolution=(1079, 2340)))
touch(Template(r"tpl1605084939526.png", record_pos=(-0.381, 0.371), resolution=(1079, 2340)))
touch(Template(r"tpl1605084945293.png", record_pos=(-0.203, 0.781), resolution=(1079, 2340)))
wait(Template(r"tpl1605084952882.png", record_pos=(-0.371, 0.373), resolution=(1079, 2340)))
touch(Template(r"tpl1605084958691.png", record_pos=(-0.398, 0.359), resolution=(1079, 2340)))
wait(Template(r"tpl1605084964920.png", record_pos=(-0.391, 0.365), resolution=(1079, 2340)))
touch(Template(r"tpl1605084967933.png", record_pos=(-0.396, 0.364), resolution=(1079, 2340)))
wait(Template(r"tpl1605084972672.png", record_pos=(-0.38, 0.368), resolution=(1079, 2340)))
touch(Template(r"tpl1605084975377.png", record_pos=(-0.37, 0.375), resolution=(1079, 2340)))
wait(Template(r"tpl1605087391338.png", record_pos=(0.0, 0.186), resolution=(1079, 2340)))
touch(Template(r"tpl1605084982109.png", record_pos=(-0.002, 0.181), resolution=(1079, 2340)))
wait(Template(r"tpl1605084988514.png", record_pos=(-0.396, 0.361), resolution=(1079, 2340)))
touch(Template(r"tpl1605084991859.png", record_pos=(-0.391, 0.373), resolution=(1079, 2340)))
wait(Template(r"tpl1605084996847.png", record_pos=(-0.385, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1605084999707.png", record_pos=(-0.396, 0.367), resolution=(1079, 2340)))
touch(Template(r"tpl1607074946480.png", record_pos=(-0.419, -0.607), resolution=(1080, 2340)))
touch(Template(r"tpl1607074965373.png", record_pos=(0.193, -0.463), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607075005801.png", record_pos=(0.185, -0.057), resolution=(1080, 2340)))
sleep(10)
touch(Template(r"tpl1607075028236.png", record_pos=(0.0, 0.496), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1607075045136.png", record_pos=(-0.002, -0.646), resolution=(1080, 2340)))
touch(Template(r"tpl1607075682347.png", record_pos=(0.007, 0.048), resolution=(1080, 2340)))
sleep(10)
touch(Template(r"tpl1607075699166.png", record_pos=(-0.002, 0.259), resolution=(1080, 2340)))
touch(Template(r"tpl1615532129161.png", record_pos=(-0.408, -0.833), resolution=(1080, 1920)))
touch(Template(r"tpl1607075777039.png", record_pos=(-0.415, -0.417), resolution=(1080, 2340)))
touch(Template(r"tpl1607075799118.png", record_pos=(0.122, -0.644), resolution=(1080, 2340)))
touch(Template(r"tpl1607075809584.png", record_pos=(-0.404, -0.77), resolution=(1080, 2340)))
touch(Template(r"tpl1607075820381.png", record_pos=(-0.002, 0.267), resolution=(1080, 2340)))
sleep(3)
while exists(Template(r"tpl1624956004367.png", record_pos=(-0.001, 0.67), resolution=(1080, 2340))):
    touch(Template(r"tpl1624956004367.png", record_pos=(-0.001, 0.67), resolution=(1080, 2340)))

    sleep(5)
    if exists(Template(r"tpl1624956030341.png", record_pos=(0.006, 0.005), resolution=(1080, 2340))):     
        break
touch(Template(r"tpl1624956030341.png", record_pos=(0.006, 0.005), resolution=(1080, 2340)))
touch(Template(r"tpl1608702399147.png", record_pos=(-0.006, 0.289), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1611730104766.png", record_pos=(-0.001, 0.306), resolution=(1079, 2340)))
sleep(3)
touch(Template(r"tpl1608702399147.png", record_pos=(-0.006, 0.289), resolution=(1080, 2340)))
sleep(2)
if exists(Template(r"tpl1615535685664.png", record_pos=(-0.185, 0.545), resolution=(1080, 1920))):
    pass
else:
    touch((400,400))
    wait(Template(r"tpl1611027052657.png", record_pos=(0.19, 0.261), resolution=(1079, 2340)))
    touch(Template(r"tpl1611027052657.png", record_pos=(0.19, 0.261), resolution=(1079, 2340)))
    sleep(8)
if exists(Template(r"tpl1615774346694.png", record_pos=(-0.038, -0.099), resolution=(1080, 1920))):
    touch(Template(r"tpl1615774358212.png", record_pos=(-0.421, -0.478), resolution=(1080, 1920)))
    touch(Template(r"tpl1615774415171.png", record_pos=(-0.403, -0.831), resolution=(1080, 1920)))
    sleep(10)
elif exists(Template(r"tpl1615535685664.png", record_pos=(-0.185, 0.545), resolution=(1080, 1920))):
    pass
else:
    touch((400,400))
    wait(Template(r"tpl1611027052657.png", record_pos=(0.19, 0.261), resolution=(1079, 2340)))
    touch(Template(r"tpl1611027052657.png", record_pos=(0.19, 0.261), resolution=(1079, 2340)))
    sleep(8)
if exists(Template(r"tpl1615774346694.png", record_pos=(-0.038, -0.099), resolution=(1080, 1920))):
    touch(Template(r"tpl1615774358212.png", record_pos=(-0.421, -0.478), resolution=(1080, 1920)))
    touch(Template(r"tpl1615774415171.png", record_pos=(-0.403, -0.831), resolution=(1080, 1920)))
    sleep(10)
elif exists(Template(r"tpl1615535685664.png", record_pos=(-0.185, 0.545), resolution=(1080, 1920))):
    pass 
else:
    touch((400,400))
    wait(Template(r"tpl1611027052657.png", record_pos=(0.19, 0.261), resolution=(1079, 2340)))
    touch(Template(r"tpl1611027052657.png", record_pos=(0.19, 0.261), resolution=(1079, 2340)))
    sleep(8)
while exists(Template(r"tpl1615535685664.png", record_pos=(-0.185, 0.545), resolution=(1080, 1920))):
    touch(Template(r"tpl1615535685664.png", record_pos=(-0.185, 0.545), resolution=(1080, 1920)))
    sleep(2)
    if exists(Template(r"tpl1608198530085.png", record_pos=(0.109, 0.425), resolution=(1080, 2340))):     
        break
touch(Template(r"tpl1608198530085.png", record_pos=(0.109, 0.425), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1608198540069.png", record_pos=(-0.006, 0.544), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1624952883550.png", record_pos=(0.007, 0.553), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1608198548988.png", record_pos=(0.231, 0.656), resolution=(1080, 2340)))
touch(Template(r"tpl1607075915022.png", record_pos=(-0.281, 0.856), resolution=(1080, 2340)))
touch(Template(r"tpl1607075923562.png", record_pos=(0.387, 0.424), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1615534195313.png", record_pos=(0.182, 0.595), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1607076416050.png", record_pos=(-0.002, 0.556), resolution=(1080, 2340)))
touch(Template(r"tpl1607076430255.png", record_pos=(0.38, 0.43), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1615774274120.png", record_pos=(0.185, 0.595), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1607076446566.png", record_pos=(0.378, 0.628), resolution=(1080, 2340)))
touch(Template(r"tpl1607076455259.png", record_pos=(0.006, 0.274), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607076469153.png", record_pos=(0.0, 0.554), resolution=(1080, 2340)))
sleep(4)
touch(Template(r"tpl1615967823531.png", record_pos=(0.0, 0.241), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607076483059.png", record_pos=(0.376, 0.63), resolution=(1080, 2340)))
touch(Template(r"tpl1615967914423.png", record_pos=(0.0, 0.239), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607076503489.png", record_pos=(0.381, 0.63), resolution=(1080, 2340)))
touch(Template(r"tpl1615967914423.png", record_pos=(0.0, 0.239), resolution=(1080, 2340)))
sleep(8)
touch(Template(r"tpl1607076522231.png", record_pos=(-0.404, 0.837), resolution=(1080, 2340)))
touch(Template(r"tpl1607076536137.png", record_pos=(-0.411, -0.263), resolution=(1080, 2340)))
touch(Template(r"tpl1607076546086.png", record_pos=(0.004, 0.546), resolution=(1080, 2340)))
touch(Template(r"tpl1608274989280.png", record_pos=(-0.285, 0.806), resolution=(1080, 2340)))
touch(Template(r"tpl1607076646556.png", record_pos=(0.378, 0.43), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1615788127079.png", record_pos=(0.183, 0.596), resolution=(1080, 1920)))
touch(Template(r"tpl1607076667119.png", record_pos=(0.389, 0.715), resolution=(1080, 2340)))
sleep(5)
touch(Template(r"tpl1615778164533.png", record_pos=(0.0, 0.531), resolution=(1080, 1920)))
touch(Template(r"tpl1607076686701.png", record_pos=(-0.011, 0.05), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1607076701138.png", record_pos=(0.37, -0.761), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1615778940763.png", record_pos=(0.185, 0.578), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1615778330604.png", record_pos=(-0.014, 0.66), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615778940763.png", record_pos=(0.185, 0.578), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1615778330604.png", record_pos=(-0.014, 0.66), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615778940763.png", record_pos=(0.185, 0.578), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1615778330604.png", record_pos=(-0.014, 0.66), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615778940763.png", record_pos=(0.185, 0.578), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1615778330604.png", record_pos=(-0.014, 0.66), resolution=(1080, 1920)))
# touch(Template(r"tpl1615778940763.png", record_pos=(0.185, 0.578), resolution=(1080, 1920)))
# sleep(5)
# touch(Template(r"tpl1615778330604.png", record_pos=(-0.014, 0.66), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615779092042.png", record_pos=(0.188, 0.582), resolution=(1080, 1920)))
sleep(5)
touch(Template(r"tpl1615778330604.png", record_pos=(-0.014, 0.66), resolution=(1080, 1920)))
touch(Template(r"tpl1615779204722.png", record_pos=(-0.193, 0.58), resolution=(1080, 1920)))
sleep(3)
touch(Template(r"tpl1607076948804.png", record_pos=(-0.404, -0.615), resolution=(1080, 2340)))
touch(Template(r"tpl1615779227050.png", record_pos=(0.186, 0.656), resolution=(1080, 1920)))
touch(Template(r"tpl1617174881755.png", record_pos=(0.197, 0.495), resolution=(1080, 2340)))
touch(Template(r"tpl1617174881755.png", record_pos=(0.197, 0.495), resolution=(1080, 2340)))
touch(Template(r"tpl1617174881755.png", record_pos=(0.197, 0.495), resolution=(1080, 2340)))
touch(Template(r"tpl1607076991262.png", record_pos=(0.193, 0.291), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607076999538.png", record_pos=(-0.187, 0.456), resolution=(1080, 2340)))
sleep(5)
touch(Template(r"tpl1607077019857.png", record_pos=(-0.006, 0.709), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1607077029910.png", record_pos=(-0.181, 0.594), resolution=(1080, 2340)))

touch(Template(r"tpl1610522711519.png", record_pos=(-0.176, -0.151), resolution=(1079, 2340)))

touch(Template(r"tpl1610522724352.png", record_pos=(0.298, 0.124), resolution=(1079, 2340)))
sleep(2)
touch(Template(r"tpl1607077221168.png", threshold=0.5, record_pos=(0.183, 0.665), resolution=(1080, 2340)))
touch(Template(r"tpl1607077232698.png", record_pos=(0.394, 0.717), resolution=(1080, 2340)))
touch(Template(r"tpl1607077243254.png", record_pos=(-0.002, 0.552), resolution=(1080, 2340)))
touch(Template(r"tpl1607077257393.png", record_pos=(-0.002, 0.859), resolution=(1080, 2340)))
touch(Template(r"tpl1607077265204.png", record_pos=(0.391, 0.23), resolution=(1080, 2340)))
touch(Template(r"tpl1607077277667.png", record_pos=(-0.152, 0.348), resolution=(1080, 2340)))
touch(Template(r"tpl1607077288299.png", record_pos=(-0.178, 0.596), resolution=(1080, 2340)))
touch(Template(r"tpl1615788081381.png", record_pos=(-0.003, 0.645), resolution=(1080, 1920)))
touch(Template(r"tpl1615788096708.png", record_pos=(0.366, 0.462), resolution=(1080, 1920)))
touch(Template(r"tpl1615788081381.png", record_pos=(-0.003, 0.645), resolution=(1080, 1920)))
sleep(4)
touch(Template(r"tpl1607077335455.png", record_pos=(-0.404, -0.767), resolution=(1080, 2340)))
sleep(3)
# touch(Template(r"tpl1607077345034.png", record_pos=(0.152, 0.346), resolution=(1080, 2340)))
# touch(Template(r"tpl1615788201500.png", record_pos=(0.346, -0.003), resolution=(1080, 1920)))
# touch(Template(r"tpl1607077373588.png", record_pos=(0.344, 0.578), resolution=(1080, 2340)))
# touch(Template(r"tpl1615788216746.png", record_pos=(-0.001, 0.65), resolution=(1080, 1920)))
# if exists(Template(r"tpl1607077402033.png", record_pos=(0.006, 0.328), resolution=(1080, 2340))):
#     touch(Template(r"tpl1607077402033.png", record_pos=(0.006, 0.328), resolution=(1080, 2340)))
# else:
#     pass
touch(Template(r"tpl1607077420223.png", record_pos=(-0.281, 0.854), resolution=(1080, 2340)))
touch(Template(r"tpl1607077019857.png", record_pos=(-0.006, 0.709), resolution=(1080, 2340)))
sleep(4)
touch(Template(r"tpl1619592584642.png", record_pos=(-0.311, -0.221), resolution=(1080, 2340)))
touch(Template(r"tpl1610522797334.png", record_pos=(0.3, 0.117), resolution=(1079, 2340)))
sleep(2)
touch(Template(r"tpl1607077221168.png", threshold=0.5, record_pos=(0.183, 0.665), resolution=(1080, 2340)))
touch(Template(r"tpl1607077232698.png", record_pos=(0.394, 0.717), resolution=(1080, 2340)))
touch(Template(r"tpl1607077243254.png", record_pos=(-0.002, 0.552), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1607077706623.png", record_pos=(0.081, 0.191), resolution=(1080, 2340)))
touch(Template(r"tpl1615788356417.png", record_pos=(0.189, 0.219), resolution=(1080, 1920)))
touch(Template(r"tpl1615788369908.png", record_pos=(0.003, 0.415), resolution=(1080, 1920)))
sleep(3)
touch(Template(r"tpl1607077747144.png", record_pos=(-0.141, 0.859), resolution=(1080, 2340)))
if exists(Template(r"tpl1615968780074.png", record_pos=(-0.011, -0.801), resolution=(1080, 2340))):
    touch(Template(r"tpl1615968795958.png", record_pos=(-0.145, 0.83), resolution=(1080, 2340)))
else:
    pass
wait(Template(r"tpl1615808103993.png", record_pos=(0.0, -0.833), resolution=(1080, 1920)))
swipe((100,1000), vector=[0.0138, -0.5083])
touch(Template(r"tpl1624961759273.png", threshold=0.85, record_pos=(-0.01, 0.553), resolution=(1080, 2340)))
touch(Template(r"tpl1607077790934.png", record_pos=(0.235, 0.62), resolution=(1080, 2340)))
wait(Template(r"tpl1606374824786.png", record_pos=(0.183, 0.317), resolution=(1080, 2340)))
touch(Template(r"tpl1606374830502.png", record_pos=(0.167, 0.313), resolution=(1080, 2340)))

sleep(10)
while exists(Template(r"tpl1606374866630.png", record_pos=(0.0, 0.835), resolution=(1080, 2340))):
    touch(Template(r"tpl1606374866630.png", record_pos=(0.0, 0.835), resolution=(1080, 2340)))
    sleep(3)
    if exists(Template(r"tpl1607073555802.png", record_pos=(-0.002, 0.061), resolution=(1080, 2340))) or exists(Template(r"tpl1607073700426.png", record_pos=(0.004, 0.322), resolution=(1080, 2340))):     
        break
sleep(3)
if exists(Template(r"tpl1607073555802.png", record_pos=(-0.002, 0.061), resolution=(1080, 2340))):
    pass
else:
    touch(Template(r"tpl1614763983679.png", record_pos=(0.005, 0.271), resolution=(1080, 2340)))
touch(Template(r"tpl1607077850241.png", record_pos=(0.235, 0.791), resolution=(1080, 2340)))
touch(Template(r"tpl1607077857138.png", record_pos=(0.176, 0.298), resolution=(1080, 2340)))
sleep(10)
while exists(Template(r"tpl1615969366783.png", record_pos=(-0.003, 0.808), resolution=(1080, 2340))):
    touch(Template(r"tpl1615969366783.png", record_pos=(-0.003, 0.808), resolution=(1080, 2340)))
    sleep(2)
    if exists(Template(r"tpl1607073555802.png", record_pos=(-0.002, 0.061), resolution=(1080, 2340))) or exists(Template(r"tpl1607073700426.png", record_pos=(0.004, 0.322), resolution=(1080, 2340))):     
        break
sleep(3)
if exists(Template(r"tpl1607073555802.png", record_pos=(-0.002, 0.061), resolution=(1080, 2340))):
    pass
else:
    touch(Template(r"tpl1607073700426.png", record_pos=(0.004, 0.322), resolution=(1080, 2340)))
touch(Template(r"tpl1607077934353.png", record_pos=(-0.215, 0.793), resolution=(1080, 2340)))
touch(Template(r"tpl1607073700426.png", record_pos=(0.004, 0.322), resolution=(1080, 2340)))
touch(Template(r"tpl1607077971844.png", record_pos=(-0.283, 0.859), resolution=(1080, 2340)))
touch(Template(r"tpl1607077980156.png", record_pos=(0.452, 0.707), resolution=(1080, 2340)))
touch(Template(r"tpl1607077986869.png", record_pos=(0.281, 0.709), resolution=(1080, 2340)))
touch(Template(r"tpl1615788705914.png", record_pos=(-0.181, 0.527), resolution=(1080, 1920)))
touch(Template(r"tpl1607078025242.png", record_pos=(0.002, 0.269), resolution=(1080, 2340)))
touch(Template(r"tpl1615788755675.png", record_pos=(-0.183, 0.274), resolution=(1080, 1920)))
touch(Template(r"tpl1615788777730.png", record_pos=(0.171, 0.277), resolution=(1080, 1920)))
# if exists(Template(r"tpl1607078063581.png", threshold=0.3, record_pos=(0.181, -0.052), resolution=(1080, 2340))):
#     sleep(3)
#     touch(Template(r"tpl1615969745325.png", record_pos=(0.229, -0.079), resolution=(1080, 2340)))
#     touch(Template(r"tpl1615969759587.png", record_pos=(0.188, 0.253), resolution=(1080, 2340)))
#     touch(Template(r"tpl1615969771361.png", record_pos=(-0.001, -0.129), resolution=(1080, 2340)))
#     touch(Template(r"tpl1615969780504.png", record_pos=(0.0, 0.235), resolution=(1080, 2340)))
# else:
#     pass
sleep(2)
touch(Template(r"tpl1620802855338.png", record_pos=(0.409, -0.357), resolution=(1080, 2340)))
touch(Template(r"tpl1615969877039.png", record_pos=(0.188, 0.259), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607083639352.png", record_pos=(-0.283, 0.857), resolution=(1080, 2340)))
touch(Template(r"tpl1607083656468.png", record_pos=(0.448, 0.702), resolution=(1080, 2340)))
touch(Template(r"tpl1607083665430.png", record_pos=(0.45, 0.709), resolution=(1080, 2340)))
touch(Template(r"tpl1608549963046.png", record_pos=(0.284, 0.653), resolution=(1080, 2340)))
touch(Template(r"tpl1615788705914.png", record_pos=(-0.181, 0.527), resolution=(1080, 1920)))
wait(Template(r"tpl1615788922225.png", record_pos=(0.196, 0.644), resolution=(1080, 1920)))
touch(Template(r"tpl1615788922225.png", record_pos=(0.196, 0.644), resolution=(1080, 1920)))
touch(Template(r"tpl1615788933514.png", record_pos=(0.183, 0.594), resolution=(1080, 1920)))
touch(Template(r"tpl1607083702995.png", record_pos=(0.38, 0.706), resolution=(1080, 2340)))
touch(Template(r"tpl1607083712343.png", record_pos=(0.0, 0.372), resolution=(1080, 2340)))
touch(Template(r"tpl1607083723203.png", record_pos=(-0.42, 0.852), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1607083809226.png", record_pos=(0.428, -0.248), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1607083817360.png", record_pos=(0.22, -0.293), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1615789224046.png", record_pos=(-0.005, 0.203), resolution=(1080, 1920)))
touch(Template(r"tpl1615970047609.png", record_pos=(0.011, 0.162), resolution=(1080, 2340)))
touch(Template(r"tpl1607083858376.png", record_pos=(0.246, -0.15), resolution=(1080, 2340)))
touch(Template(r"tpl1607083866596.png", record_pos=(0.0, 0.657), resolution=(1080, 2340)))
touch(Template(r"tpl1607083878518.png", record_pos=(0.191, 0.285), resolution=(1080, 2340)))
touch(Template(r"tpl1615789261161.png", record_pos=(-0.003, 0.2), resolution=(1080, 1920)))
touch(Template(r"tpl1607083897243.png", record_pos=(-0.406, -0.767), resolution=(1080, 2340)))
touch(Template(r"tpl1607083907349.png", record_pos=(-0.404, -0.769), resolution=(1080, 2340)))
touch(Template(r"tpl1607083917001.png", record_pos=(0.313, 0.657), resolution=(1080, 2340)))
touch(Template(r"tpl1615788705914.png", record_pos=(-0.181, 0.527), resolution=(1080, 1920)))
touch(Template(r"tpl1607083934775.png", record_pos=(-0.002, -0.185), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1607083942305.png", record_pos=(0.191, 0.281), resolution=(1080, 2340)))
sleep(2)
touch(Template(r"tpl1615788705914.png", record_pos=(-0.181, 0.527), resolution=(1080, 1920)))
touch(Template(r"tpl1607083962102.png", record_pos=(0.126, -0.622), resolution=(1080, 2340)))
touch(Template(r"tpl1607084010457.png", record_pos=(-0.372, -0.613), resolution=(1080, 2340)))
touch(Template(r"tpl1607084020480.png", record_pos=(0.376, 0.05), resolution=(1080, 2340)))
sleep(3)
touch(Template(r"tpl1615788922225.png", record_pos=(0.196, 0.644), resolution=(1080, 1920)))
sleep(1)
touch(Template(r"tpl1607084047604.png", record_pos=(0.385, 0.711), resolution=(1080, 2340)))
touch(Template(r"tpl1615789326417.png", record_pos=(-0.003, 0.708), resolution=(1080, 1920)))
touch(Template(r"tpl1607084131017.png", record_pos=(-0.42, 0.859), resolution=(1080, 2340)))
touch(Template(r"tpl1607084139145.png", record_pos=(0.311, 0.419), resolution=(1080, 2340)))
touch(Template(r"tpl1615788705914.png", record_pos=(-0.181, 0.527), resolution=(1080, 1920)))
touch(Template(r"tpl1615789418020.png", record_pos=(0.183, 0.659), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615789366036.png", record_pos=(0.004, 0.197), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1607084173902.png", record_pos=(0.009, -0.596), resolution=(1080, 2340)))
touch(Template(r"tpl1615789418020.png", record_pos=(0.183, 0.659), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615789366036.png", record_pos=(0.004, 0.197), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1607084199980.png", record_pos=(0.241, -0.6), resolution=(1080, 2340)))
touch(Template(r"tpl1615789418020.png", record_pos=(0.183, 0.659), resolution=(1080, 1920)))
sleep(2)
touch(Template(r"tpl1615789366036.png", record_pos=(0.004, 0.197), resolution=(1080, 1920)))
touch(Template(r"tpl1607084226284.png", record_pos=(0.443, -0.691), resolution=(1080, 2340)))
touch(Template(r"tpl1615789488570.png", record_pos=(-0.419, -0.671), resolution=(1080, 1920)))
touch(Template(r"tpl1615789498570.png", record_pos=(-0.006, -0.715), resolution=(1080, 1920)))
touch(Template(r"tpl1615789507324.png", record_pos=(-0.003, 0.094), resolution=(1080, 1920)))
touch(Template(r"tpl1615789514970.png", record_pos=(0.005, 0.219), resolution=(1080, 1920)))

webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/2e9c5652-5bee-4579-9d4f-31b85c20b362"
feishu = FeiShutalkChatbot(webhook)
feishu.send_text(r"APK自动化执行成功，报告查看：http://10.10.102.242/report/stg2apk.log/")