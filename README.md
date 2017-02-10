# My social network graph

![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/FB.png)
Here is an example of a plot where you can find the number of connection my friends have together : <a href="https://plot.ly/~pradogusto/2.embed" target="_blank">https://plot.ly/~pradogusto/2.embed</a>
![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/new_plot.png)
## Facebook scrapping

For the first part of this project, I use Selenium to scrap my Facebook account. The goal is to see how much is Facebook open for scrapping data, maybe for other purpose later. Selenium is a very practical language, especially to move quickly from a Facebook profile to an other.

## Friends

After all the scrapping that took few hours, here are some results about my network.
I have 162 friends, me and my 162 friends have 1983 relations together. As you can see on the following picture, we can easily partition the graph into communities only by looking at the connections. Anyway, we use a detection community algorithm and it appears that the results correspond to my vision of my Facebook friends.
![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/my_net.png)
Find the interactive version of communities [HERE](https://plot.ly/~pradogusto/0.embed)

## Friends & Friends of Friends 

Figures are more serious, problem is bigger and computer slower. If we count all my friends and all my friends' friends we have almost 54.000 people. I realize then that 45.000 of them share only 1 friends with me. To simplify the final graph, I remove all people that have less than 4 friends in common with me. Here is the result, we can clearly see communities even without running an algorithm.

![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/larger_net.png)
Find yourself [there](https://plot.ly/~pradogusto/6.embed)

Thank you to Jonas Racine who shared its code on it's [github](https://github.com/jonasracine) and gave me the idea for this little work !
