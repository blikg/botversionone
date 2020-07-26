#### Bot discord 
###### 26 de Mayo 2020 
######## Copyright reserved
########## contanto francisco_apb@hotmail.com

##-----------------Bilbiotecas importadas--------------------------------
import discord
from discord.ext import commands
import datetime
import math
import requests
from bs4 import BeautifulSoup
##------------------------------------------------------------------------
chara = '>'
bot = commands.Bot(command_prefix=chara, description = "Este es el Ayuda bot") ##Inicializando el bot y definimos el simbolo y el mensaje de descripcion
bot.remove_command('help')
##------------------Funciones de informacion----------------------------
#funcion para conocer el ping y saber si esta en linea el bot
@bot.command()
async def transis(ctx):
    await ctx.send(f'Tor ! {round(bot.latency*1000)}ms')
#Informacion relevante del server y del bot
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description ="Bot realizado por Francisco Puente"+"\n"+"Usar >help o >funciones para su utilización", timestamp =datetime.datetime.utcnow(),color= discord.Color.blue())
    embed.add_field(name="Server Creado en", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Propietario del servidor", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del Server", value=f"{ctx.guild.region}")
    embed.set_thumbnail(url="http://www.teslaelectronics.cl/770-large_default/transistor-mmbf5457-jfet-smd.jpg")
    await ctx.send(embed=embed)
#funciones ayuda
@bot.command()
async def help(ctx):
    await ctx.send("**Funciones de información.**"
                   +"\n"+chara+"transis: Devuelve Tor ! y su latencia."
                   +"\n"+chara+"info: Devuelve información relevante."
                   +"\n"+"**Funciones de monedas.**"
                   +"\n"+chara+"usdcl: Devuelve Dolar observado del día."
                   +"\n"+chara+"ufcl: Devuelve valor de la UF del día."
                   +"\n"+chara+"eurocl: Devuelve valor de la Euro del día."
                   +"\n"+"**Funciones matemáticas.**"
                   +"\n"+chara+"suma x y: Adición, ejem: >suma x y , resultado: x+y, siendo x,y e |R, %f."
                   +"\n"+chara+"sumas x+y...+z: Adición multiple, ejem: >suma x+y+z , resultado: x+y+z, siendo x,y,z e |R, %f."
                   +"\n"+chara+"resta: Sustración, ejem: >resta x y  , resultado: x-y siendo x,y e |R %f."
                   +"\n"+chara+"mul: producto, ejem: >mul x y  ,  resultado: x*y siendo x,y e |R, %f"
                   +"\n"+chara+"muls x*y*...*z: producto multiple, ejem: >mul x*y*z  ,  resultado: x*y*z siendo x,y,z e |R, %f"
                   +"\n"+chara+"div: cociente, ejem: >div x y  ,  resultado: x/y siendo x,y e |R con y!= 0,%f."
                   +"\n"+chara+"seno x: Devuelve el seno de x radianes."
                   +"\n"+chara+"cos x: Devuelve el coseno de x radianes."
                   +"\n"+chara+"sqrt x: Devuelve la raíz cuadrada de x, ejem: >sqrt 4  , resultado: 2.0."
                   +"\n"+chara+"pow x y: Devuelve x elevado a la potencia y"
                   +"\n"+chara+"exp x: Devuelve e elevado a la potencia x , donde e = 2.718281 ..."
                   +"\n"+chara+"pi: La constante matemática π = 3.141592 ..."
                   +"\n"+chara+"e: La constante matemática e = 2.718281 ..."
                   +"\n"+"**Funciones sociales.**"
                   +"\n"+chara+"uma: Revuelve página web UMAYOR"
                   +"\n"+chara+"insta: Ingresando nombre en instagram desvuelve el link completo"
                   +"\n"+chara+"ElSignificadoDeLaVida: Devuelve el significado de la vida"
                   )
@bot.command()
async def ayuda(ctx):
    await ctx.send("**Funciones de información.**"
                   +"\n"+chara+"transis: Devuelve Tor ! y su latencia."
                   +"\n"+chara+"info: Devuelve información relevante."
                   +"\n"+"**Funciones de monedas.**"
                   +"\n"+chara+"usdcl: Devuelve Dolar observado del día."
                   +"\n"+chara+"ufcl: Devuelve valor de la UF del día."
                   +"\n"+chara+"eurocl: Devuelve valor de la Euro del día."
                   +"\n"+"**Funciones matemáticas.**"
                   +"\n"+chara+"suma x y: Adición, ejem: >suma x y , resultado: x+y, siendo x,y e |R, %f."
                   +"\n"+chara+"sumas x+y...+z: Adición multiple, ejem: >suma x+y+z , resultado: x+y+z, siendo x,y,z e |R, %f."
                   +"\n"+chara+"resta: Sustración, ejem: >resta x y  , resultado: x-y siendo x,y e |R %f."
                   +"\n"+chara+"mul: producto, ejem: >mul x y  ,  resultado: x*y siendo x,y e |R, %f"
                   +"\n"+chara+"muls x*y*...*z: producto multiple, ejem: >mul x*y*z  ,  resultado: x*y*z siendo x,y,z e |R, %f"
                   +"\n"+chara+"div: cociente, ejem: >div x y  ,  resultado: x/y siendo x,y e |R con y!= 0,%f."
                   +"\n"+chara+"seno x: Devuelve el seno de x radianes."
                   +"\n"+chara+"cos x: Devuelve el coseno de x radianes."
                   +"\n"+chara+"sqrt x: Devuelve la raíz cuadrada de x, ejem: >sqrt 4  , resultado: 2.0."
                   +"\n"+chara+"pow x y: Devuelve x elevado a la potencia y"
                   +"\n"+chara+"exp x: Devuelve e elevado a la potencia x , donde e = 2.718281 ..."
                   +"\n"+chara+"pi: La constante matemática π = 3.141592 ..."
                   +"\n"+chara+"e: La constante matemática e = 2.718281 ..."
                   +"\n"+"**Funciones sociales.**"
                   +"\n"+chara+"uma: Revuelve página web UMAYOR"
                   +"\n"+chara+"insta: Ingresando nombre en instagram desvuelve el link completo"
                   +"\n"+chara+"ElSignificadoDeLaVida: Devuelve el significado de la vida"
                   )
    
aaa=  ""+"\n"+chara+""
#funcion help
#@bot.command(pass_context=True)
#async def help(ctx):
#    autor = ctx.message.author

#    embed = discord.Embed(colour = discord.Colour.orange())
#    embed.set_author(name='Help')
#    embed.add_field(name=chara+'Info', value = 'Origen y Autores', inline=False)
#    await bot.send_message(autor, embed=embed)

##--------------------------------------------------------------------    
#Funcion dolar observable
@bot.command()
async def usdcl(ctx):
    urldolar = 'https://www.bcentral.cl/'
    page = requests.get(urldolar)

    soup = BeautifulSoup(page.content,'html.parser')

    eq=soup.find_all('p', class_='mb-0 text-center')

    lista=list()
    count = 0
    for i in eq:
        if count < 20:
        
            lista.append(i.text)
        else:
            break
        count+=1
    await ctx.send("USD: " + str(lista[5]).strip())

#Funcion UF
@bot.command()
async def ufcl(ctx):
    urldolar = 'https://www.bcentral.cl/'
    page = requests.get(urldolar)

    soup = BeautifulSoup(page.content,'html.parser')

    eq=soup.find_all('p', class_='mb-0 text-center')

    lista=list()
    count = 0
    for i in eq:
        if count < 20:
        
            lista.append(i.text)
        else:
            break
        count+=1
    await ctx.send("UF: "+str(lista[1]).strip())
#Funcion EURO
@bot.command()
async def eurocl(ctx):
    urldolar = 'https://www.bcentral.cl/'
    page = requests.get(urldolar)

    soup = BeautifulSoup(page.content,'html.parser')

    eq=soup.find_all('p', class_='mb-0 text-center')

    lista=list()
    count = 0
    for i in eq:
        if count < 20:
        
            lista.append(i.text)
        else:
            break
        count+=1
    await ctx.send("EURO: "+str(lista[7]).strip())



    
##--------Operaciones Matematicas---------------------

#Funcion suma
@bot.command()
async def leo(ctx):
    await ctx.send("gay")

#Funcion suma
@bot.command()
async def china(ctx):
    await ctx.send("lena")
    
#Funcion suma
@bot.command()
async def suma(ctx,  numero1:float,numero2:float):
    await ctx.send(numero1+numero2)
#Funcion sumas
@bot.command()
async def sumas(ctx,  numero1: str):
    numero1 =numero1.split('+')
    
    result = 0
    for number in numero1:
        result += float(number)
    
    await ctx.send(result)
#Funcion resta
@bot.command()
async def resta(ctx,  numero1 : float, numero2 : float):
    await ctx.send(numero1 - numero2)
#Funcion Muntiplicacion
@bot.command()
async def mul(ctx,  numero1 : float, numero2 : float):
    await ctx.send(numero1 * numero2)
#Funcion Muntiplicaciones
@bot.command()
async def muls(ctx,  numero1 : str):
    numero1 = numero1.split('*')
    result = 1
    for number in numero1:
        result=result*float(number)
    await ctx.send(result)

    
#funcion Division
@bot.command()
async def div(ctx,  numero1 : float, numero2 : float):
    if numero2!=0:
        await ctx.send(numero1 / numero2)
    else:
        await ctx.send('Indefinido')
#funcion Seno
@bot.command()
async def seno(ctx,  numero1 : float):
    resultado = math.sin(numero1)
    await ctx.send(resultado)
#funcion conseno
@bot.command()
async def cos(ctx,  numero1 : float):
    resultado = math.cos(numero1)
    await ctx.send(resultado)
    
#funcion raiz cuadrada
@bot.command()
async def sqrt(ctx,  numero1 : float):
    resultado = math.sqrt(numero1)
    await ctx.send(resultado)

#funcion potencia
@bot.command()
async def pow(ctx,  numero1 : float,numero2 : float):
    resultado = math.pow(numero1,numero2)
    await ctx.send(resultado)

#Funcion Exponencial
@bot.command()
async def exp(ctx,  numero1 : float):
    resultado = math.exp(numero1)
    await ctx.send(resultado)
#Funcion Pi
@bot.command()
async def pi(ctx):
    await ctx.send(math.pi)

#Funcion e
@bot.command()
async def e(ctx):
    await ctx.send(math.e)

#---------------Funciones sociales-------------
#Funcion que pagina umayor
@bot.command()
async def uma(ctx):
    await ctx.send('https://www.umayor.cl/um/')
#Funcion Instagrama 
@bot.command()
async def insta(ctx, instagram):
    await ctx.send('https://www.instagram.com/'+instagram+'/')
#Funciones del significado de la vida
@bot.command()
async def ElSignificadoDeLaVida(ctx):
    await ctx.send('42 panes')
@bot.command()
async def chupalo(ctx):
    await ctx.send('piñera')
#events
@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Member(name="Bot miembro",url="https://www.instagram.com/francho.pte/"))
    print('Wena conchetumate')

    

bot.run('NzM0OTEyMTkzNTA1Nzg3OTI2.XxYmZA.JxAdr1NbXdqzXGjYFxOC9XocA5o')
