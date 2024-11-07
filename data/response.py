from mitmproxy import http, ctx
import mimetypes

# 要替换的本地图片路径
local_image_path = "/home/mitmproxy/renji.jpg"

def response(flow: http.HTTPFlow) -> None:
    """
    修改特定域名特定响应头的响应
    """
    if flow.request.pretty_url.startswith("https://thirdqq.qlogo.cn/ek_qqapp/"):
        if flow.response.headers.get("Last-Modified") == "Mon, 01 Jan 1990 00:00:00 GMT":
            ctx.log.info(f"修改响应：{flow.request.pretty_url}")

            # 复制原始响应
            new_response = flow.response.copy()

            # 获取图片类型
            image_type = mimetypes.guess_type(local_image_path)[0]

            # 修改响应内容
            with open(local_image_path, "rb") as f:
                new_response.content = f.read()
                new_response.headers["Content-Type"] = image_type
                new_response.headers["Content-Length"] = str(len(new_response.content))

            # 将修改后的响应替换原始响应
            flow.response = new_response 
