from django.db import models


# Create your models here

class Player(models.Model):
    Player_id = models.IntegerField()
    Name = models.CharField(max_length=500)
    Type = models.CharField(max_length=654)
    Country = models.CharField(max_length=50)
    Debut_year = models.IntegerField()
    ODI_rankings = models.IntegerField()
    T20_rankings = models.IntegerField()
    Test_rankings = models.IntegerField()
    Profile = models.TextField()
    Batting_style = models.CharField(max_length=66)
    BasePrice = models.IntegerField()
    CurrentPrice = models.IntegerField()
    Player_img_1 = models.ImageField(upload_to='images/', max_length=500)
    Player_img_2 = models.ImageField(upload_to='images_1/', max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.Player_id


class TEST_STATS(models.Model):
    Player_id = models.IntegerField()
    test_matches = models.IntegerField()
    test_runs = models.IntegerField()
    test_fours = models.IntegerField()
    test_sixes = models.IntegerField()
    test_ducks = models.IntegerField()
    test_balls = models.IntegerField()
    test_wicket = models.IntegerField()
    test_economy = models.IntegerField()
    test_5w = models.IntegerField()


class ODI_STATS(models.Model):
    Player_id = models.IntegerField()
    odi_matches = models.IntegerField()
    odi_runs = models.IntegerField()
    odi_fours = models.IntegerField()
    odi_sixes = models.IntegerField()
    odi_ducks = models.IntegerField()
    odi_balls = models.IntegerField()
    odi_wicket = models.IntegerField()
    odi_economy = models.IntegerField()
    odi_5w = models.IntegerField()


class T20I_STATS(models.Model):
    Player_id = models.IntegerField()
    t20i_matches = models.IntegerField()
    t20i_runs = models.IntegerField()
    t20i_fours = models.IntegerField()
    t20i_sixes = models.IntegerField()
    t20i_ducks = models.IntegerField()
    t20i_balls = models.IntegerField()
    t20i_wicket = models.IntegerField()
    t20i_economy = models.IntegerField()
    t20i_3w = models.IntegerField()


class IPL_STATS(models.Model):
    Player_id = models.IntegerField()
    ipl_matches = models.IntegerField()
    ipl_runs = models.IntegerField()
    ipl_fours = models.IntegerField()
    ipl_sixes = models.IntegerField()
    ipl_ducks = models.IntegerField()
    ipl_balls = models.IntegerField()
    ipl_wicket = models.IntegerField()
    ipl_economy = models.IntegerField()
    ipl_3w = models.IntegerField()
