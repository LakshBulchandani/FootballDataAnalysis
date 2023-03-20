import mysql.connector
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "userAdmin",
    database = "pl_data"
    )

cursorObject = dataBase.cursor()

st.set_page_config(layout="wide")

image = Image.open("PLTeams.png")
st.image(image)

st.title("Football Data Analysis")

st.write("Welcome to Football Data Analysis! This site is used to plot different parameters of Premier League football data.")

teamHexColour = ['#ef0107','#670e36','#8b0304','#e30613','#005daa','#034694','#27409b','#274488','#d0d0d0','#ffcd00','#003090','#c8102e','#6cabdd','#da291c','#241f20','#e53233','#d71920','#132257','#7a263a','#fdb913']

text_data = dict(Squad="The club's name", MP="Number of matches played",W="Number of wins by the club",D="Number of draws by the club",L="Number of losses by the club",GF="Goals For - Goals scored by the club",GA="Goals Against - Goals scored against the club",GD="Goal Difference - The difference between goals scored and goals conceded : GF - GA",Pts="Total points gained for matches played by the club. Win = 3, Draw = 1, Loss = 0",PtsMP="Points per match played. Calculated as Pts/MP",xG="Expected Goals. It measures the statistical quality of goalscoring chances and the likelihood of them being scored",xGA="Expected Goals Against. It measures the statistical quality of goalscoring chances and the likelihood of them being scored against the club",xGD="Expected Goal Difference. The difference between xG for and xG conceded. Calculated as xG - xGA",xGDP90="Expected Goal Difference per match played. Calculated as xGD/MP",Players="Number of players currently under contract of the club",Age="Average age of current players in the club",Poss="Average Possession maintained by the club per match",Goals="Number of goals scored",Assist="Contribution by a player which helps to score a goal",GPlusA="The sum of goals and assists. Calculated as Goals+Assists",GPK="Non Penalty Goals scored. Calculated as Goals-Penalty Goals",PK="Penalty Goals scored",PKatt="Penalty Kicks attempted",CrdY="Number of yellow cards shown to the players of a club",CrdR="Number of red cards shown to the players of a club",npxG="Non Penalty Expected Goals. Measures the statistical quality of non-penalty goal scoring chances",xAG="Expected Assisted Goals. Measures the statistical quality of a contribution by a player which may lead to a goalscoring chance",Fouls="Number of fouls commited by players of a club")

query = "SELECT * FROM defensestats"
cursorObject.execute(query)

defense = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'Tkl' , 'TklW' , 'TklDef' , 'TklMid' , 'TklAtt' , 'ChlTkl' , 'ChlAtt' , 'ChlTklPerc' , 'ChlLost' , 'Blocks' , 'ShBlk' , 'PassBlk' , 'Int' , 'TklPlusInt' , 'Clr' , 'Err']
)

query = "SELECT * FROM generalstats ORDER BY Squad"
cursorObject.execute(query)

general = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Rk' , 'Squad' , 'MP' , 'W' , 'D' , 'L' , 'GF' , 'GA' , 'GD' , 'Pts' , 'PtsPM' , 'xG' , 'xGA' , 'xGD' , 'xGDP90']
)

query = "SELECT * FROM gkadvanced"
cursorObject.execute(query)

gkadv = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'MP' , 'FKCon' , 'CKCon' , 'OGCon' , 'PSxG' , 'PSxGPSoT' , 'PSxGNet' , 'PSxG90' , 'LaunchCmp' , 'LaunchAtt' , 'LaunchCmpPerc' , 'GKAttPass' , 'GKThrPass' , 'LaunchPassPerc' , 'GKPassAvgLen' , 'GKAtt','GKLaunchPerc','GkAvgLen','CrsOpp','CrsStp','CrsStpPerc','OPA','OPAP90','GKAvgDist']
)

query = "SELECT * FROM gkstats"
cursorObject.execute(query)

gkstats = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'MP' , 'GA' , 'GA90' , 'SoTA' , 'Saves' , 'SavesPerc' , 'CS' , 'CSPerc' , 'PKConatt' , 'PKACon' , 'PKsv' , 'PKm' , 'PKSavePerc']
)

query = "SELECT * FROM miscstats"
cursorObject.execute(query)

misc = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'CrdY' , 'CrdR' , '2CrdY' , 'Fouls' , 'FoulDrawn' , 'Offside' , 'Cross' , 'Int' , 'TklW' , 'PKwon' , 'PKcon' , 'OGCon' , 'Recoveries' , 'AirWon' , 'AirLost' , 'AirWonPerc']
)

query = "SELECT * FROM passingstats"
cursorObject.execute(query)

passing = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'PassCmp' , 'PassAtt' , 'PassCmpPerc' , 'TotDist' , 'PrgDist' , 'ShrtPassCmp' , 'ShrtPassAtt' , 'ShrtPassCmpPerc' , 'MedPassCmp' , 'MedPassAtt' , 'MedPassCmpPerc' , 'LongPassCmp' , 'LongPassAtt' , 'LongPassCmpPerc' , 'Assist' , 'xAG','xA','AMinusxAG','KP','PassFinThrd','PPA','CrsPA','PrgP']
)

query = "SELECT * FROM passtypes"
cursorObject.execute(query)

passt = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'PassAtt' , 'PassLive' , 'PassDead' , 'FKPass' , 'ThroughPass' , 'Switch' , 'Crs' , 'ThrowIn' , 'Corner' , 'CornerIn' , 'CornerOut' , 'CornerStr' , 'PassCmp' , 'PassOffside' , 'PassBlocks']
)

query = "SELECT * FROM possessionstats"
cursorObject.execute(query)

possession = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' ,'Poss' ,'Touches' , 'TouchDefPen' , 'TouchDef3rd' , 'TouchMid3rd' , 'TouchAtt3rd' , 'TouchAttPen' , 'TouchLive' , 'TakeOnAtt' , 'TakeOnSucc' , 'TakeOnSuccPerc' , 'Tackled' , 'TackledPerc' , 'Carries' , 'TotalDist' , 'PrgDist','PrgC','CarryFinThrd','CarryPA','Miscontrol','Disposessed','Received','PrgR']
)

query = "SELECT * FROM scagca"
cursorObject.execute(query)

scagca = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'SCA' , 'SCA90' , 'GCA' , 'GCA90']
)

query = "SELECT * FROM shootingstats"
cursorObject.execute(query)

shooting = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Players' , 'Goals' , 'Shots' , 'SoT' , 'SoTPerc' , 'ShP90' , 'SoTP90' , 'GperSh' , 'GperSoT' , 'ShotDist' , 'FKShots' , 'PKGls' , 'PKatt' , 'xG' , 'npxG' , 'npxGPerSh' , 'GMinusxG','npGMinusxG']
)

query = "SELECT * FROM standardstats"
cursorObject.execute(query)

standard = pd.DataFrame(
    cursorObject.fetchall(),
    columns = ['Squad' , 'Age' , 'Poss' , 'Goals' , 'Assist' , 'GPlusA' , 'GPK' , 'PK' , 'PKatt' , 'CrdY' , 'CrdR' , 'xG' , 'npxG' , 'xAG' , 'npxGxAG' , 'PrgC' , 'PrgP' , 'Gls90','Ast90','GA90','GPK90','GAPK90','xG90','xAG90','xGxAG90','npxG90','npxGxAG90']
)

stats = general.join(defense, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(gkadv, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(gkstats, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(misc, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(passing, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(passt, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(possession, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(scagca, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(shooting, rsuffix="DROP").filter(regex="^(?!.*DROP)")
stats = stats.join(standard, rsuffix="DROP").filter(regex="^(?!.*DROP)")

def Plotter(P1='Fouls',P2='CrdY'):
    Parameter1 = P1
    Parameter2 = P2
    hover_text = []
    for i in range(0,20):
        hover_text.append("{}:{}<br>{}:{}<br>Ratio:{}".format(Parameter1,stats[Parameter1][i],Parameter2,stats[Parameter2][i],round(stats[Parameter1][i]/stats[Parameter2][i],3)))

    fig = go.Figure()
    
    for i in range(0,20):
        fig.add_trace(go.Scatter(
            x=[stats[Parameter1][i]],
            y=[stats[Parameter2][i]],
            text=hover_text[i],
            mode='markers',
            showlegend=True,
            marker=dict(
            color=teamHexColour[i],
            size=30
            ),
            name=stats['Squad'][i]
        ))

    fig.update_layout(
        title="{} vs {}".format(Parameter1,Parameter2),
        xaxis=dict(
            title=Parameter1
        ),
        yaxis=dict(
            title=Parameter2
        )
    )
    fig.add_shape(
        type='line',line_color="#000000",line_width=3,opacity=1,line_dash='dot',
        x0=stats[Parameter1].min(),x1=stats[Parameter1].max(),y0=stats[Parameter2].mean(),y1=stats[Parameter2].mean()
    )

    fig.add_shape(
        type='line',line_color="#000000",line_width=3,opacity=1,line_dash='dot',
        x0=stats[Parameter1].mean(),x1=stats[Parameter1].mean(),y0=stats[Parameter2].min(),y1=stats[Parameter2].max()
    )
    st.plotly_chart(fig)

st.title("Premier League Raw Data")

st.write("Number of Columns = {}".format(stats.shape[1]))

st.dataframe(stats.sort_values(by=['Rk']))

st.title("Graph Plotter")

st.write("An X-axis vs Y-axis Graph can be plotted by selecting the parameters from First Parameter and Second Parameter")

col1, col2, col3 = st.columns([1.2,2,1.2],gap="large")

with col1:
    option1 = st.selectbox(
        'First Parameter',
        (stats.columns)
    )
    st.title(option1)
    if option1 in text_data:
        st.write(text_data[option1])

with col3:
    option2 = st.selectbox(
        'Second Parameter',
        (stats.columns),
    )
    st.title(option2)
    if option2 in text_data:
        st.write(text_data[option2])

with col2:
    Plotter(option1,option2)

dataBase.close()