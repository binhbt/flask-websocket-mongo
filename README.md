# flask-websocket-mongo
Run docker: docker-compose up --build  
Run wscat connect to server as socket client  
wscat -c ws://0.0.0.0:82/echo/111  
wscat -c ws://0.0.0.0:82/echo/222  
wscat -c ws://0.0.0.0:82/echo/333  
Push Message via rest api  
`curl --location --request POST 'http://0.0.0.0:82/push' \
--header 'Content-Type: text/plain' \
--data-raw '{"client_id":"111", "message":"joined", "type":"provider_noti"}'`  
Client with id 111 will receive message  

Get list message  
curl --location --request GET 'http://0.0.0.0:82/api/v1/notifications/111'  
Have fun!
