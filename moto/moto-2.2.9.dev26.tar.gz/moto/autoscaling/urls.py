from __future__ import unicode_literals
from .responses import AutoScalingResponse

url_bases = [r"https?://autoscaling\.(.+)\.amazonaws\.com"]

url_paths = {"{0}/$": AutoScalingResponse.dispatch}
