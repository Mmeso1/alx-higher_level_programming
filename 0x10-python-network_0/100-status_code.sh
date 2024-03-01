#/bin/bash
# displays only the status code of the url request reponse
curl -so /dev/null -w "%{http_code}" "$1"
