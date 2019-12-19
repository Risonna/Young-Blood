define p = Character('???', color="#c8ffc8")
define e = Character('вставить', color="#c8ffc8")
define main = Character("[mainname]")
define pol = 0
image hall_1:
        "background hall_1.jpg"
image library:
        "background library.jpg"
image zoo:
        "background zoo.jpg"
image fish:
        "background fish.jpg"
image food1:
        "background food1.jpg"
image corridor1:
        "background corridor1.jpg"
image map:
        "interactive map.jpg"
image korpus2_1:
        "background korpus2_1.jpg"
image korpus2_2:
        "background korpus2_2.jpg"
image korpus5_1:
        "background korpus5_1.jpg"

        
'''screen binoculars:
    modal True
    vbox:
        xalign 1.0 yalign 0.5
        textbutton "up" action SetVariable("bg_yalign", max(-0.2, (bg_yalign-0.1) )  )#максимальные и минимальные значения надо подобрать так, чтобы картинка на заднем фоне не "убегала" за края бинокля
        hbox:
            textbutton "left" action SetVariable("bg_xalign", max(-0.2, (bg_xalign-0.1) )  )
            null width 20
            textbutton "right" action SetVariable("bg_xalign", min( 1.2, (bg_xalign+0.1) )  )
        textbutton "down" action SetVariable("bg_yalign", min( 1.2, (bg_yalign+0.1) )  )
        textbutton "X" action [Hide("binoculars"), Hide("back_view") ]'''
    
'''screen back_view:
    add "bg" zoom 2.0 xalign bg_xalign yalign bg_yalign'''
    
screen korpus2:
    imagebutton xalign 0.463 yalign 0.235:
        #эта картинка используется когда кнопка не в фокусе
        idle ("images/interactive korpus2.png")
        #эта картинка используется когда кнопка в фокусе
        hover ("images/interactive korpus2_aimed.png")
        #это действие произойдет если на кнопку навести курсор
        #hovered ShowMenu('images/interactive korpus2_aimed.png')
        #это действие произойдет если на кнопку навести курсор, а потом убрать
        #unhovered ShowMenu('images/interactive korpus2_aimed.png')
        #и собственно действие которое будет происходить при нажатии
        action Jump("korpus2_1")
        
screen korpus5:
    imagebutton xalign 0.571 yalign 0.5855:
        idle ("images/interactive korpus5.png")
        hover ("images/interactive korpus5_aimed.png")
        action Jump("korpus5")
        
label splashscreen:
    $ renpy.pause(0)
    scene black
    show text "ПОМОГИ НАМ БОЖЕ" 
    with dissolve
    with Pause(1.0)

    hide text 
    with dissolve

    return
    
label start:
    stop music
#Если понадобится в будущем сделать выбор пола для обращение, нужно  использовать if not pol для женщины и всё остальное для мужчины
    menu:
        "Как к вам обращаться?"

        "Он.":
            $pol = 1

        "Она.":
            $pol = pol
            
    p "Привет! Рада видеть тебя в нашем университете! Сегодня я буду твоим экскурсоводом. Меня зовут вставить! А тебя, значит..?"

    python:
        mainname = renpy.input("Введите имя") 
        mainname = mainname.strip()

        if not mainname:
            mainname = "Саша"

    if mainname == "Саша":
        "Вы не ввели имя, теперь вас будут звать Саша"

    e "[mainname], значит? Здорово!"

    if not pol:
        e "Давай я тебе здесь всё покажу! Сначала пройдёмся по основным местам,
        а потом ты сама выберешь, куда бы ты хотела сходить."
    
    else:
        e "Давай я тебе здесь всё покажу! Сначала пройдёмся по основным местам,
        а потом ты сам выберешь, куда бы ты хотел сходить."

    scene hall_1
    show hall_1
    with dissolve
    
    play music "audio/2song.mp3"

    e "Сейчас мы находимся в главном холле Кемеровского Государтвенного Университета
    - КемГУ ^-^ Как тебе?"
    e "Обычно здесь очень людно. Также это место часто преображается в зависимости
    от праздников или посещающих нас гостей."
    e "Выглядит мило, правда? И это только начало. Уже представляешь, что ждёт нас дальше?"
    e "М-м? Не впечатлило? Ну, тогда я покажу тебе кое-что ещё. Пойдём за мной."
    
    hide hall_1
    
    play sound "audio/walking in a building.mp3"
    
    show library
    with Fade(1.0, 0.0, 1.0)
    
    e "Тсс, не шуми! Это библиотека на 2-м этаже. Здесь ты можешь отдохнуть в тишине после
    тяжелого учебного дня. Также тут можно взять необходимую тебе книжку, но не забудь вернуть!"
    e "Эээ... Нет, здесь нет журналов такого рода..."
    e "Так, о чем это я? Ах, да. Почитать и отдохнуть."
    e "Кстати, это не единственная библиотека в этом корпусе! Спустившись на первый этаж и пройдя
    чуть вдаль по корридору ты сможешь её найти. Но давай посмотрим более жив... интересные места!"
    
    hide library
    
    show zoo
    with dissolve
    
    e "Ты, наверное, не думал, что у нас есть свой зоопарк ^-^ "
    e "Конечно, он не такой большой, как в других зоопарках,
    но всё же помогает студентам немного отвлечься ^-^"
    menu:
        e "Тебе нравится?"
        
        "Да":
            main "Ну.."
            hide zoo
            show fish
            with dissolve
            e "ДА КОНЕЧНО НРАВИТСЯ! Ты посмотри, какие они все милые uwu"
        "Нет":
            main "Ну.."
            hide zoo
            show fish
            with dissolve
            e "ДА КОНЕЧНО НРАВИТСЯ! Ты посмотри, какие они все милые uwu"
    e "Пойдём дальше!"
    
    hide zoo
    
    scene corridor1
    play sound "audio/walking in a building.mp3"
    show corridor1
    with Fade(1.0, 0.5, 1.0)
    
    if not pol:
        e "Ты, случайно, не голодна?"
    else:
        e "Ты, случайно, не голоден?"
    
    menu:
        "Да, я бы не отказалась перекусить." if not pol:
            main "Совсем немного..."
            e "Замечательно, я как раз хотела показать тебе столовую! Иди за мной."
        "Я думаю, нет.":
            main "Нет..."
            #play sound tummy
            "..."
            e "Хи-хи. Следуй за мной."
        "Да, я бы не отказался перекусить." if pol:
            main "Совсем немного..."
            e "Замечательно, я как раз хотела показать тебе столовую! Иди за мной."
    
    hide corridor1
    
    show food1
    with Fade(1.0, 0.0, 1.0)
    
    e "Устройся поудобнее, [mainname], а я пока схожу и возьму тебе что-нибудь перекусить uwu"
    
    "[e] ушла, а я решаю осмотреться."
    "Отведя взгляд в сторону, я решаю прислушаться к разговору за соседним столиком..."
    
    p "..."
    
    hide food1
    
    show map
    with fade
    
    show screen korpus2
    show screen korpus5  
    window hide
    pause
    
    return

label korpus5:
    hide screen korpus5
    hide screen korpus2
    show korpus5_1
    with fade
    
    "У вас нет happiness"
    
    return

label korpus3:
    "death end"
    return

label korpus2_1:
    hide screen korpus5
    hide screen korpus2
    
    show korpus2_1
    with fade
    
    "Здесь должны быть какие-то деййствия"
    
    

    #здесь уходят в столовку или куда там надо было

    "здесь кончается пробная версия,
    спасибо за прохождение."

    return