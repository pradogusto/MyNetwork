# My social network graph
This presentation resume a project I’ve made where I display my Facebook network and do some analysis on it. It is coded in python, find the code in the jupiter Notebook /facebook_network.ipynb, you’ll have some explanations. Libraries used are Selenium for scrapping, NetworkX for building graphs, Plotly for visualization.

![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/FB.png)
Here is a plot where you can find the number of connection my friends have together : https://plot.ly/~pradogusto/0.embed

![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/new_plot.png)
## Facebook scrapping

For the first part of this project, I use Selenium to scrap my Facebook account. The goal is to see how much is Facebook open for scrapping data, maybe for other purpose later. Finally, Selenium is a very practical library, especially to move quickly from a Facebook profile to an other, but Facebook changes quite often the code of its pages and sometimes the same code doesn’t work the day after, if you don’t change one line where the web element you want to select has changed. You can find a little demo of scrapping [here] (https://www.youtube.com/watch?v=KurcdkvC9U4). Functions can be found in /scrap_function.py

## Friends

After the scrapping that took a few hours, here are some results about my network.
I have 162 friends, me and my 162 friends have 1983 relations together. As you can see on the picture above, we can easily partition the graph into communities only by looking at the connections. Anyway, we use a detection community algorithm and it appears that the results correspond to my vision of my Facebook friends.
![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/my_net.png)

Find the interactive version of communities <p><a href="plot.ly/~pradogusto/2.embed" target="_blank">https://plot.ly/~pradogusto/2.embed</a></p> !

## Friends & Friends of Friends 

Figures are more serious, problem is bigger and computer slower. If we count all my friends and all my friends' friends we have almost 54.000 people. I realize then that 45.000 of them share only 1 friends with me. To simplify the final graph, I remove all people that have less than 4 friends in common with me. Here is the result, we can clearly appearing 3 communities even without running an algorithm. For curious, you are likely to find yourself [there](https://plot.ly/~pradogusto/6.embed).

![alt tag](https://github.com/pradogusto/MyNetwork/blob/master/pic/larger_net.png)

Thank you to Jonas Racine who shared its code on it's [github](https://github.com/jonasracine) and gave me the idea for this little work !
