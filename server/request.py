class Request:
    def __init__(self, content):
        self.content = content.decode("utf-8")
        self.fileDirectory = ""
        self.mime = "text/plain"
        self.type = ""
        self.allMimes = ["text/plain", "text/html", "text/html", "image/png", "audio/aac", "application/x-abiword", "application/x-freearc", "image/avif", "video/x-msvideo", "application/vnd.amazon.ebook", "application/octet-stream", "image/bmp", "application/x-bzip", "application/x-bzip2", "application/z-cdf", "application/z-csh", "text/css", "text/csv", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/vnd.ms-fontobject", "application/epub+zip", "application/gzip", "image/gif", "image/vnd.microsoft.icon", "text/calender", "application/java-archive", "image/jpeg", "image/jpeg", "text/javascript", "application/json", "application/ld+json", "audio/midi", "audio/x-midi", "text/javascript", "audio/mpeg", "video/mp4", "video/mpeg", "application/vnd.apple.installer+xml", "application/vnd.oasis.opendocument.presentation", "application/vnd.oasis.opendocument.spreadsheet", "application/vnd.oasis.opendocument.text", "audio/ogg", "video/ogg", "application/ogg", "audio/opus", "font/otf", "application/pdf", "application/x-httpd-php", "application/vnd.ms-powerpoint", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "application/vnd.rar", "application/rtf", "application/x-sh", "image/svg+xml", "application/x-tar", "image/tiff", "image/tiff", "video/mp2t", "font/ttf", "application/vnd.visio", "audio/wav", "audio/webm", "video/webm", "image/webp", "font/woff", "font/woff2", "application/xhtml+xml", "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/xml", "application/vnd.mozilla.xul+xml", "application/zip", "video/3gpp", "video/3gpp2", "application/z-7z-compressed"]
    
    def parseType(self):
        if self.content.split()[0] == "GET":
            self.type = "GET"

    def parseFileDirectory(self):
        self.fileDirectory = self.content.split("\n")[0].split()[1]
        if self.fileDirectory == "/" or self.fileDirectory[len(self.fileDirectory)-1] == "/":
            self.fileDirectory += "index.html"
        elif len(self.fileDirectory.split("/")[len(self.fileDirectory.split("/"))-1].split(".")) == 1:
            self.fileDirectory += "/index.html"
    def parseMime(self):
        end = self.fileDirectory.split(".")[1]
        