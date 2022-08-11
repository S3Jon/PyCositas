#!/bin/bash
# File: server.sh
# Author: Doffyj <doffyj@protonmail.com>
# Date: 10/08/2022 @ 23:10:58
# Last Modified Date: 11/08/2022 @ 20:09:23
# Last Modified By: Doffyj <doffyj@protonmail.com>

#!/bin/bash
wanIp="$(curl https://ipinfo.io/ip 2>/dev/null)";
echo "La ip de tu servidor es ${wanIp}:8000"
start chrome http://localhost:8000
python -m http.server 8000
