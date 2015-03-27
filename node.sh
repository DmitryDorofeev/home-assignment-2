java -jar selenium-server.jar \
 -role hub &

java -jar selenium-server.jar \
 -role node \
 -hub http://localhost:4444/grid/register \
 -Dwebdriver.chrome.driver="./chromedriver" \
 -browser browserName=chrome,maxInstances=1 \
 -browser browserName=firefox,maxInstances=1 &