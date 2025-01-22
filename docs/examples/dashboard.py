"""FrankenUI Dashboard Example"""

from fasthtml.common import *
from monsterui.all import *
from fasthtml.svg import *
import numpy as np
import plotly.express as px
import pandas as pd
import numpy as np

def generate_chart(num_points):
    dates = pd.date_range('2024-01-01', periods=num_points)
    df = pd.DataFrame({
        'Date':    dates,
        'Revenue': (np.random.exponential(1, num_points) + np.sin(np.linspace(0,4,num_points))*0.3).cumsum(),
        'Users':   (np.random.exponential(0.8, num_points) + np.cos(np.linspace(0,4,num_points))*0.2).cumsum(),
        'Growth':  (np.random.exponential(0.6, num_points) + np.sin(np.linspace(0,6,num_points))*0.4).cumsum()})
    fig = px.area(df, x='Date', y=df.columns[1:], template='plotly_white', line_shape='spline')
    fig.update_layout(
        margin=dict(l=20,r=20,t=20,b=20), hovermode='x unified',
        showlegend=True, legend_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    
    return fig.to_html(include_plotlyjs=True,  full_html=False, config={'displayModeBar': False})

def InfoCard(title, value, change): return Card(H3(value),P(change, cls=TextFont.muted_sm), header = H4(title))

rev = InfoCard("Total Revenue", "$45,231.89", "+20.1% from last month")
sub = InfoCard("Subscriptions", "+2350", "+180.1% from last month")
sal = InfoCard("Sales", "+12,234", "+19% from last month")
act = InfoCard("Active Now", "+573", "+201 since last hour")

info_card_data = [("Total Revenue", "$45,231.89", "+20.1% from last month"),
                   ("Subscriptions", "+2350", "+180.1% from last month"),
                   ("Sales", "+12,234", "+19% from last month"),
                   ("Active Now", "+573", "+201 since last hour")]

top_info_row = Grid(*[InfoCard(*row) for row in info_card_data])

def AvatarItem(name, email, amount):
    return DivFullySpaced(
        DivLAligned(
            DiceBearAvatar(name, 9,9),
            Div(P(name, cls=TextFont.bold_sm), 
                P(email, cls=TextFont.muted_sm))),
        Div(amount, cls="ml-auto font-medium"))

recent_sales = Card(
    Div(cls="space-y-8")(
        *[AvatarItem(n,e,d) for (n,e,d) in (
            ("Olivia Martin",   "olivia.martin@email.com",   "+$1,999.00"),
            ("Jackson Lee",     "jackson.lee@email.com",     "+$39.00"),
            ("Isabella Nguyen", "isabella.nguyen@email.com", "+$299.00"),
            ("William Kim",     "will@email.com",            "+$99.00"),
            ("Sofia Davis",     "sofia.davis@email.com",     "+$39.00"))]),
    header=Div(H3("Recent Sales"),P("You made 265 sales this month.", cls=TextFont.muted_sm)),
    cls='col-span-3')

teams = [["Alicia Koch"],['Acme Inc', 'Monster Inc.'],['Create a Team']]

opt_hdrs = ["Personal", "Team", ""]

team_dropdown = UkSelect(
    Optgroup(Option(A("Alicia Koch")), label="Personal Account"),
    Optgroup(Option(A("Acme Inc")), Option(A("Monster Inc.")), label="Teams"),
    Option(A("Create a Team")),
    cls='flex items-center')

hotkeys = [('Profile','⇧⌘P'),('Billing','⌘B'),('Settings','⌘S'),('New Team', ''), ('Logout', '')]

def NavSpacedLi(t,s): return NavCloseLi(A(DivFullySpaced(P(t),P(s,cls=TextFont.muted_sm))))

avatar_dropdown = Div(
      DiceBearAvatar('Alicia Koch',8,8),
      DropDownNavContainer(
          NavHeaderLi('sveltecult',NavSubtitle("leader@sveltecult.com")),
          *[NavSpacedLi(*hk) for hk in hotkeys],))

top_nav = NavBar(
    Div(team_dropdown, *map(lambda x: Li(A(x)), ["Overview", "Customers", "Products", "Settings"])),
    DivLAligned(avatar_dropdown, Input(placeholder='Search')))

def page():
    return Div(cls="space-y-4")(
        top_nav,
        H2('Dashboard'),
        TabContainer(
            Li(A("Overview"),cls='uk-active'),
            *map(lambda x: Li(A(x)), ["Analytics", "Reports", "Notifications"]),
            alt=True),
        top_info_row,
        Grid(
            Card(Safe(generate_chart(100)),cls='col-span-4'),
            recent_sales,
            gap=4,cols=7))

dashboard_homepage = page()
