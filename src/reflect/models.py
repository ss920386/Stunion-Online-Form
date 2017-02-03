from django.db import models

# Create your models here.


class Reflection(models.Model):
	name = models.CharField(max_length=50, blank = True, null = True)
	email = models.EmailField()

	CATEGORY_CHOICES = [
        ("FACILITY", "學校設備"),
        ("RESTAURANT", "餐廳食物"),
        ("ACADEMY", "課業學習"),
        ("ACTIVITY", "學生活動"),
        ("OTHER", "其他"),
    ]
	category = models.CharField(max_length=10, choices= CATEGORY_CHOICES)
	content = models.TextField(max_length=500, blank = False, null = True)
	advice = models.TextField(max_length=500, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now=True)
	state = models.IntegerField(default = 0)
	important = models.BooleanField(default=False)
	#replies = models.ManyToManyField(Reply)

	def __str__(self):
		return str(self.timestamp)

class Reply(models.Model):
	user = models.CharField(max_length = 20) # 回覆的使用者
	content = models.CharField(max_length = 500) # 回覆內容
	timestamp = models.DateTimeField(auto_now=True) # 創建時間
	reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE, default=None, null=True)
	#reflectionID = models.IntegerField(unique=True) # 該問題的id
	def __str__(self):
		return str(self.timestamp)