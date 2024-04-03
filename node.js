var http = require("http");
var fs = require("fs");

http.createServer(requestListener:function (req, res) {
    fs.readFile("jsverilerim.html",function(err,data){
        res.writeHead(statusCode:200,headers:{"Content-Type"})
        res.write(data);
        res.end();

    });

}
).listen(8000);