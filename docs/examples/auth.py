from fasthtml.common import *
from monsterui.all import *
from fasthtml.svg import *

def page():    
    left = Div(cls="col-span-1 hidden flex-col justify-between bg-zinc-900 p-8 text-white lg:flex")(
        Div(cls=(TextT.bold,TextT.default))("Acme Inc"),
        Blockquote(cls="space-y-2")(
            P(cls=TextT.large)('"This library has saved me countless hours of work and helped me deliver stunning designs to my clients faster than ever before."'),
            Footer(cls=TextT.small)("Sofia Davis")))

    right = Div(cls="col-span-2 flex flex-col p-8 lg:col-span-1")(
        DivRAligned(Button("Login", cls=ButtonT.ghost)),
        DivCentered(cls='flex-1')(
            Container(
                DivVStacked(
                    H3("Create an account"),
                    P("Enter your email below to create your account", cls=TextFont.muted_sm)),
                Form(
                    Input(placeholder="name@example.com"),
                    Button(Span(cls="mr-2", uk_spinner="ratio: 0.54"), "Sign in with Email", cls=(ButtonT.primary, "w-full"), disabled=True),
                    DividerSplit("Or continue with",cls=TextFont.muted_sm),
                    Button(UkIcon('github',cls='mr-2'), "Github", cls=(ButtonT.default, "w-full")),
                    cls='space-y-6'),
                P(
                    "By clicking continue, you agree to our ",
                    A(cls=AT.muted, href="#demo")("Terms of Service")," and ",
                    A(cls=AT.muted, href="#demo")("Privacy Policy"),".",
                    cls=(TextFont.muted_sm,"text-center")),
                cls="space-y-6")))
    
    return Grid(left,right,cols=2, gap=0,cls='h-screen')

auth_homepage = page()
