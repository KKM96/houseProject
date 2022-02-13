from django.db import models

# Create your models here.


class Region(models.Model):
    id = models.IntegerField
    reg1 = models.CharField(max_length=200)
    reg2 = models.CharField(max_length=200)
    reg3 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return self.reg1


class MonthBusan(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()
    rent_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'month_busan'

    def __float__(self):
        return self.bldg_area


class MonthIncheon(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()
    rent_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'month_incheon'

    def __float__(self):
        return self.bldg_area


class MonthGyeonggi(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()
    rent_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'month_gyeonggi'

    def __float__(self):
        return self.bldg_area


class MonthDaejeon(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()
    rent_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'month_daejeon'

    def __float__(self):
        return self.bldg_area


class MonthSeoul(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()
    rent_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'month_seoul'

    def __float__(self):
        return self.bldg_area


class SellBusan(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sell_busan'

    def __float__(self):
        return self.bldg_area


class SellIncheon(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sell_incheon'

    def __float__(self):
        return self.bldg_area


class SellGyeonggi(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sell_gyeonggi'

    def __float__(self):
        return self.bldg_area


class SellDaejeon(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sell_daejeon'

    def __float__(self):
        return self.bldg_area


class SellSeoul(models.Model):
    dname = models.CharField(max_length=100)
    menuGubun = models.CharField(max_length=100)
    bldg_nm = models.CharField(max_length=200)
    bldg_area = models.FloatField(max_length=100)
    year = models.IntegerField()
    deal_mm = models.IntegerField()
    sum_amt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sell_seoul'

    def __float__(self):
        return self.bldg_area

