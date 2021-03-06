# Data Visualizer Dash
https://dashcx.felippefn.repl.co/

### _Project: dashboard made for specific analysis of the net promoter score._

- Dashboard in Python language, styled in Css, created to visualize and process data
- obs: the project is in portuguese.

## _This project works like this:_

<!--
Sem o cursor do mouse:
![Dashboard-NPS](https://user-images.githubusercontent.com/79763393/156893430-0711505a-8d12-4d06-a825-e15ea3766c00.gif)
-->

<!--
Com o cursor do mouse:
-->
![Dashboard-NPS-Mouse](https://user-images.githubusercontent.com/79763393/156893599-2f316e23-fac9-47f3-b169-dd7c35699168.gif)

## _How to use_

To use this dashboard, you just need to visit the link down below.

```
https://dashcx.felippefn.repl.co/
```
## _How the dashboard works_

The python script found in the file [main.py](https://github.com/Felippefn/Data-visualizer-Dash/blob/main/main.py), reads a file in excel, extracts column by column the necessary information and computates it as a data model for visualization. After extracting the information, the NPS (Net Promoter Score) is calculated. In this way, the user can verify all the information of the conditions established in this topic:

![image](https://user-images.githubusercontent.com/79763393/156893824-afb68f48-edea-4060-aab3-db2608e89751.png)

You can choose the <b>month</b>, <b>year</b> and <b>communication channel with the customer</b>.


## _How does the NPS calculation work?_

The NPS calculation is very simple. Percentage of Promoters - Percentage of Detractors (%Promoters - %Detractors).

<b>The function of this calculation is that:</b>

```python
def nps_calculate(list_):
    detractor = []
    neutral = []
    promoter = []

    for item in list_:
        if item < 7:
            detractor.append(item)
        elif item > 8:
            promoter.append(item)
        else:
            neutral.append(item)

    total = detractor + promoter + neutral
    nps = ((len(promoter)/len(total))*100) - \
        ((len(detractor)/len(total))*100)
    if nps >= 0:
        nps = nps + 0.45
    else:
        nps = nps - 0.45
    return nps

```

particular recognition to<br>Vinicius (https://github.com/Vinicius-Santoro) who made this increadible README<br>
Pedro (https://github.com/pedrokrivochein) who supported me with some bugs and problems.
