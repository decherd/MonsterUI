"""FrankenUI Music Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../example_music.ipynb.

# %% auto 0
__all__ = ['music_items', 'file_dd_items', 'edit_actions', 'view_dd_data', 'account_dd_data', 'music_headers',
           'listen_now_albums', 'made_for_you_albums', 'music_content', 'tabs', 'discoved_data', 'library_data',
           'playlists_data', 'sb', 'music_homepage', 'MusicLi', 'AlbumImg', 'AlbumFooter', 'Album', 'create_album_grid',
           'podcast_tab', 'LAlignedIconTxts', 'MusicSidebarLi', 'page']

# %% ../example_music.ipynb
from fasthtml.common import *
import fasthtml.common as fh
from fh_frankenui import *
from fh_frankenui.core import *
 

# %% ../example_music.ipynb
def MusicLi(t,hk=''): return Li(A(DivFullySpaced(t,P(hk,cls=TextFont.muted_sm))))

music_items = [("About Music", ""),("Preferences", "⌘"),("Hide Music", "⌘H"),("Hide Others", "⇧⌘H"),("Quit Music", "⌘Q")]

file_dd_items = [("New", ""),("Open Stream URL", "⌘U"),("Close Window", "⌘W"),("Library", ""),("Import", "⌘O"),
    ("Burn Playlist to Disc", ""),("Show in Finder", "⇧⌘R"),("Convert", ""),("Page Setup", "Print")]

edit_actions = [("Undo", "⌘Z"),("Redo", "⇧⌘Z"),("Cut", "⌘X"),("Copy", "⌘C"),
    ("Paste", "⌘V"),("Select All", "⌘A"),("Deselect All", "⇧⌘A")]

view_dd_data = ["Show Playing Next", "Show Lyrics", "Show Status Bar", "Hide Sidebar", "Enter Full Screen"]

account_dd_data = [Span("Switch Account", cls="ml-6"), [SpacedPP("Andy"), LAlignedTxtIcon("Benoit", 'plus-circle', 0.5, icon_right=False), SpacedPP("Luis")],
                   SpacedPPs("Manage Family"), SpacedPPs("Add Account")]

# %% ../example_music.ipynb
music_headers =NavBarContainer(
    NavBarLSide(
        NavBarNav(
            Li(A("Music"),NavBarNavContainer(map(lambda x: MusicLi(*x), music_items))),
            Li(A("File"),NavBarNavContainer(map(lambda x: MusicLi(*x), file_dd_items))),
            Li(A("Edit")),
                NavBarNavContainer(
                    *map(lambda x: MusicLi(*x), edit_actions),
                    Li(A(DivFullySpaced("Smart Dictation",UkIcon("mic")))),
                    Li(A(DivFullySpaced("Emojis & Symbols",UkIcon("globe"))))),
            Li(A("View"),
               NavBarNavContainer(map(lambda x: MusicLi(x), view_dd_data))),
            Li(A("Account"),
                NavBarNavContainer(
                    NavHeaderLi("Switch Account"),
                    MusicLi("Andy"),
                    MusicLi("Benoit"),
                    MusicLi("Luis"),
                    MusicLi("Manage Family"),
                    MusicLi("Add Account"))),
        cls='space-x-4')))

# %% ../example_music.ipynb
def AlbumImg(url):
    return Div(cls="overflow-hidden rounded-md")(Img(cls="transition-transform duration-200 hover:scale-105", src=url))

def AlbumFooter(title, artist):
    return Div(cls='space-y-1')(P(title,cls=TextT.bold),P(artist,cls=TextT.muted))

def Album(url,title,artist):
    return Div(AlbumImg(url),AlbumFooter(title,artist))

# %% ../example_music.ipynb
listen_now_albums = (("Roar", "Catty Perry"), ("Feline on a Prayer", "Cat Jovi"),("Fur Elise", "Ludwig van Beethovpurr"),("Purrple Rain", "Prince's Cat"))

made_for_you_albums = [("Like a Feline", "Catdonna"),("Livin' La Vida Purrda", "Ricky Catin"),("Meow Meow Rocket", "Elton Cat"),
        ("Rolling in the Purr", "Catdelle",),("Purrs of Silence", "Cat Garfunkel"),("Meow Me Maybe", "Carly Rae Purrsen"),]
    

# %% ../example_music.ipynb
def create_album_grid(albums, cols=4):  
    return Grid(*[Div(cls="uk-grid-small")(
                Div(cls="overflow-hidden rounded-md")(
                    Img(cls="transition-transform duration-200 hover:scale-105", src=img_url, alt="")),
                Div(cls="space-y-1 text-sm")(
                    H3(album['title'], cls="font-medium leading-none"),
                    P(album['artist'], cls="text-xs text-muted-foreground"))) for album in albums],
                cols,gap=4)

# %% ../example_music.ipynb
_album = lambda t,a: Album('https://ucarecdn.com/e5607eaf-2b2a-43b9-ada9-330824b6afd7/music1.webp',t,a)

music_content = (Div(H3("Listen Now"), cls="mt-6 space-y-1"),
                    P("Top picks for you. Updated daily.",cls=TextFont.muted_sm),
                    UkHLine(),
                    Grid(*[_album(t,a) for t,a in listen_now_albums], cols=4, cols_lg=4,cls='gap-8'),
                    Div(H3("Made for You"), cls="mt-6 space-y-1"),
                    P("Your personal playlists. Updated daily.", cls=TextFont.muted_sm),
                    UkHLine(),
                    Grid(*[_album(t,a) for t,a in made_for_you_albums], cols=6))

# %% ../example_music.ipynb
tabs = TabContainer(
    Li(A('Music', href='#'),cls='uk-active'),
    Li(A('Podcasts', href='#')),
    Li(A('Live', cls='opacity-50'), cls='uk-disabled'),
    uk_switcher='connect: #component-nav; animation: uk-animation-fade',
    alt=True)

# %% ../example_music.ipynb
def podcast_tab():
    return Div(
        Div(cls="space-y-3")(
            H3("New Episodes"),
            P("Your favorite podcasts. Updated daily.", cls=TextFont.muted_sm)),
        Div(cls="my-4 h-[1px] w-full bg-border"),
        Div(cls="uk-placeholder flex h-[450px] items-center justify-center rounded-md",uk_placeholder=True)(
            Div(cls="text-center space-y-6")(
                UkIcon("microphone", 3),
                H4("No episodes added"),
                P("You have not added any podcasts. Add one below.", cls=TextFont.muted_sm),
                Button("Add Podcast", cls=ButtonT.primary))))

# %% ../example_music.ipynb
def LAlignedIconTxts(ns, icns): return [Li(A(LAlignedIconTxt(n,i))) for n,i in zip(ns,icns)]

# %% ../example_music.ipynb
discoved_data = [("play-circle","Listen Now"), ("binoculars", "Browse"), ("rss","Radio")]
library_data = [("play-circle", "Playlists"), ("music", "Songs"), ("user", "Made for You"), ("users", "Artists"), ("bookmark", "Albums")]
playlists_data = [("library","Recently Added"), ("library","Recently Played")]

# %% ../example_music.ipynb
def MusicSidebarLi(icon, text): return Li(A(DivLAligned(UkIcon(icon), P(text),cls='space-x-2')))
sb = NavContainer(
    NavHeaderLi(H3("Discover")),*[MusicSidebarLi(*o) for o in discoved_data],
    NavHeaderLi(H3("Library")),*[MusicSidebarLi(*o) for o in library_data],
    NavHeaderLi(H3("Playlists")),*[MusicSidebarLi(*o) for o in playlists_data],
    cls=(NavT.primary,'space-y-3','pl-8'),
)

# %% ../example_music.ipynb
def page():
    return Div(Container(music_headers,cls='py-8'),UkHSplit(),
        Grid(sb,
            Div(cls="col-span-4 border-l border-border")(
                Div(cls="px-8 py-6")(
                    Div(cls="flex items-center justify-between")(
                        Div(cls="max-w-80")(tabs),
                        Button(cls=ButtonT.primary)(Span(cls="mr-2 size-4")(UkIcon('circle-plus')),"Add music")),
                    Ul(id="component-nav", cls="uk-switcher")(
                        Li(*music_content),
                        Li(podcast_tab())))),
            cols=5))

# %% ../example_music.ipynb
music_homepage = page()
