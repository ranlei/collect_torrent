#!/bin/bash
# Downloads .torrent files from kickass.com links  
# following redirects and getting the actual torrent  
# filename 

AGENT="'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'"
function usage(){
    echo "Usage: $0 [kickass Torrent URL]"
    exit 1
}
if [ ! -n "$1" ]
then
        usage
fi
name=`echo $1 | sed 's/.*kat.ph.//'`".torrent"
curl --globoff --compressed -A '$AGENT' -L --post302 $1 > $name
transmission -m $name
