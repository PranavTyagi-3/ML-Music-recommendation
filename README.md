# ML_music-recommendation

It happens that you are listening to a song and you liked it very much and then wish to listen some similar songs. When you search for those similar songs, those are based on popularity, user rating etc. but you just wanted a similar song whether popular or not. So we have made a project where user can directly go to and search for similar songs without any hassle of login or any other stuff

![image](https://user-images.githubusercontent.com/89564642/206619084-12b4aa64-d5bb-4c94-9c72-a45b26887c63.png)

![image](https://user-images.githubusercontent.com/89564642/206619100-e0549bab-026c-426e-8f3b-34ab897fe750.png)

Basically we first made a dataset containing 1000s of songs along with their audio features such as acoustics, valence, energy, etc. After that, we made recommendations using two methods namely Vector Distance and K-means. In vector distance, we converted our songs into vectors and calculated distance between the user entered song and other songs in our database. Then we made the recommendation by sorting the songs based on vector distance giving top 5 songs. In the K-means method, we applied K-means machine learning algorithm to find clusters in our database. When you enter a song, we again use the K-means algorithm to predict which cluster the entered song will belong to and then we have displayed 5 random songs from that cluster. The total 10 songs are then displayed on the user screen
