# Data type	Django model type	Database DDL	Description - Validation - Notes
# SQLite	MySQL	PostgreSQL	Oracle	
# Binary	models.BinaryField()	BLOB NOT NULL	longblob NOT NULL	bytea NOT NULL	BLOB NULL	Creates a blob field to store binary data (e.g. images, audio or other multimedia objects)
# Boolean	models.BooleanField()	bool NOT NULL	bool NOT NULL	boolean NOT NULL	NUMBER(1) NOT NULL CHECK ("VAR" IN (0,1))	Creates a boolean field to store True/False (or 0/1) values
# Boolean	models.NullBooleanField()	bool NULL	bool NULL	boolean NULL	NUMBER(1) NULL CHECK (("VAR" IN (0,1)) OR ("VAR" IS NULL))	Works just like BooleanField but also allows NULL values
# Date/time	models.DateField()	date NOT NULL	date NOT NULL	date NOT NULL	DATE NOT NULL	Creates a date field to store dates
# Date/time	models.TimeField()	time NOT NULL	time NOT NULL	time NOT NULL	TIMESTAMP NOT NULL	Creates a time field to store times.
# Date/time	models.DateTimeField()	datetime NOT NULL	datetime NOT NULL	timestamp with time zone NOT NULL	TIMESTAMP NOT NULL	Creates a datetime field to store dates with times
# Date/time	models.DurationField()	bigint NOT NULL	bigint NOT NULL	interval NOT NULL	INTERVAL DAY(9) TO SECOND(6) NOT NULL	Creates a field to store periods of time.
# Number	models.AutoField()	integer NOT NULL AUTOINCREMENT	integer AUTO_INCREMENT NOT NULL	serial NOT NULL	NUMBER(11) NOT NULL & also creates a SEQUENCE and TRIGGER to increase the field	Creates an integer that autoincrements, primarly used for custom primary keys
# Number	models.BigIntegerField()	bigint NOT NULL	bigint NOT NULL	bigint NOT NULL	NUMBER(19) NOT NULL	Create a big integer to fit numbers between -9223372036854775808 to 9223372036854775807. This range may vary depending on the DB brand
# Number	models.DecimalField(decimal_places=X,max_digits=Y)	decimal NOT NULL	numeric(X, Y) NOT NULL	numeric(X, Y) NOT NULL	NUMBER(10, 3) NOT NULL	Enforces a number have a maximum X digits and Y decimal points Creates a decimal field to store decimal numbers. Note both X and Y arguments are required, where the X argument represents the maximum number of digits to store and the Y argument represents the number of decimal places to store.
# Number	models.FloatField()	real NOT NULL	double precision NOT NULL	double precision NOT NULL	DOUBLE PRECISION NOT NULL	Creates a column to store floating-point numbers.
# Number	models.IntegerField()	integer NOT NULL	integer NOT NULL	integer NOT NULL	NUMBER(11) NOT NULL	Creates a column to store integer numbers.
# Number	models.PositiveIntegerField()	integer unsigned NOT NULL	integer UNSIGNED NOT NULL	integer NOT NULL CHECK ("VAR" >= 0)	NUMBER(11) NOT NULL CHECK ("VAR" >= 0)	Enforces values from 0 to 2147483647 Works just like IntegerField but limits values to positive numbers
# Number	models.PositiveSmallIntegerField()	smallint unsigned NOT NULL	smallint UNSIGNED NOT NULL	smallint NOT NULL CHECK ("VAR" >= 0)	NUMBER(11) NOT NULL CHECK ("VAR" >= 0)	Enforces values from 0 to 32767 Works just like IntegerField and the specialized PositiveIntegerField but limits numbers to a smaller positive range.
# Number	options.SmallIntegerField()	smallint NOT NULL	smallint NOT NULL	smallint NOT NULL	NUMBER(11) NOT NULL	Enforces a number is in the range from -32768 to 32767 Works just like IntegerField but in a smaller integer range.
# Text	models.CharField(max_length=N)	varchar(N) NOT NULL	varchar(50) NOT NULL	varchar(50) NOT NULL	NVARCHAR2(50) NULL	Creates a text column, where the max_length argument is required to specify the maximum length in characters.
# Text	models.TextField()	text NOT NULL	longtext NOT NULL	text NOT NULL	NCLOB NULL	Creates a text field to store text.
# Text (Specialized)	models.CommaSeparatedIntegerField(max_length=50)	varchar(N) NOT NULL	varchar(N) NOT NULL	varchar(N) NOT NULL	NVARCHAR2(N) NULL	Enforces the string a CSV of integers.Works just like CharField except Django enforces the string be a comma separated value of integers prior to interacting with the database (e.g. 3,54,54,664,65)
# Text (Specialized)	models.EmailField()	varchar(254) NOT NULL	varchar(254) NOT NULL	varchar(254) NOT NULL	NVARCHAR2(254) NULL	Enforces the text is a valid email with the internal Django EmailValidator to determine what is and isn't a valid. Works just like CharField defaulting to a max_length of 254 characters and also enforces the string is a valid email.
# Text (Specialized)	models.FileField()	varchar(100) NOT NULL	varchar(100) NOT NULL	varchar(100) NOT NULL	NVARCHAR2(100) NULL	Enforces and provides various utilities to handle files (e.g. opening/closing file, upload location,etc). Works just like CharField defaulting to a max_length of 100 characters and also enforces the string is a valid file.
# Text (Specialized)	models.FilePathField()	varchar(100) NOT NULL	varchar(100) NOT NULL	varchar(100) NOT NULL	NVARCHAR2(100) NULL	Enforces and provides various utilities to limit choices of filenames in certain filesystem directories. Works just like CharField defaulting to a max_length of 100 characters and also enforces the string is a valid file in a filesystem directory.
# Text (Specialized)	models.ImageField()	varchar(100) NOT NULL	varchar(100) NOT NULL	varchar(100) NOT NULL	NVARCHAR2(100) NULL	Enforces and provides various utilities to handle image files (e.g. getting the height & width) Works just like CharField and the specialized FileField defaulting to a max_length of 100 characters and also enforces the string is a valid image. Note this field requires the presence of the Pillow Python library (e.g. pip install Pillow).
# Text (Specialized)	models.GenericIPAddressField()	char(39) NOT NULL	char(39) NOT NULL	inet NOT NULL	VARCHAR2(39) NULL	Enforces and provides various utilities to only accept valid IPv4 or IPv6 addresses (e.g. 198.10.22.64 and FE80::0202:B3FF:FE1E:8329, as well as utilities like unpack_ipv4 and protocol) Works just like CharField defaulting to a max_length of 39 characters and enforces the string is a valid IP address.
# Text (Specialized)	models.SlugField()	varchar(50) NOT NULL	varchar(50) NOT NULL	varchar(50) NOT NULL	NVARCHAR2(50) NULL	Enforces a string is a slug string, which is a string that only contains letters, numbers, underscores or hyphens. Works just like CharField defaulting to a max_length of 50 characters and ensure the provided string is a slug -- a concept that's typically used to cleanse URL strings that contains spaces and other potentially invalid character like letter with accents.
# Text (Specialized)	models.URLField()	varchar(200) NOT NULL	varchar(200) NOT NULL	varchar(200) NOT NULL	NVARCHAR2(200) NULL	Enforces the provided text value is a valid URL Works just like CharField defaulting to a max_length of 200 characters and enforces the string is a valid URL
# Text (Specialized)	models.UUIDField()	char(32) NOT NULL	char(32) NOT NULL	uuid NOT NULL	VARCHAR2(32) NOT NULL	Enforces the provided text is a Universally unique identifiers (UUID) Works just like CharField defaulting to a max_length of 32 characters and enforces the value is a UUID.


from pydoc import describe
from turtle import title
from unicodedata import category
from django.db import models

class News(models.Model):
    url = models.CharField(max_length=100)


class NewsUrls(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()

class Sentences(models.Model):
    sentence_de= models.CharField(max_length=1000)
    sentence_jp= models.CharField(max_length=1000)
    category_id= models.IntegerField(0,null=True)
    url_id = models.IntegerField(0,null=True)

class Words(models.Model):
    word_de= models.CharField(max_length=1000)
    word_jp= models.CharField(max_length=1000)
    category_id= models.IntegerField(0,null=True)
    url_id = models.IntegerField(0,null=True)


class Apis(models.Model):
    name= models.CharField(max_length=1000)
    describe= models.CharField(max_length=1000)
    url= models.URLField()
    usrname= models.TextField()
    apikey=models.TextField()
    form=models.TextField()

class data_NewsApi(models.Model):
    title= models.CharField(max_length=100)
    descripriotn=models.CharField(max_length=1000)
    url=models.URLField()
    publishedAt=models.DateField()
    content=models.TextField(max_length=10000)
    api_id=models.IntegerField(0,null=True)
