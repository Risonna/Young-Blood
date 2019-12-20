define p = Character('???', color="#c8ffc8")
define e = Character('Ульяна', color="#c8ffc8")
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
image hall_2:
        "background hall_2.jpg"
image hall_3:
        "background hall_3.jpg"
image bloch:
        "background bloch.jpg"
image food2:
        "background food2.jpg"
image bloch:
        "background bloch.jpg"
image korpus3:
        "background korpus3.jpg"
image korpus5:
        "background korpus5.jpg"
image sprite_in_thoughts:
        "sprites/sprite ul3.png"
image sprite_facepalm:
        "sprites/sprite ul2_1.png"
image sprite_closed_eye:
        "sprites/sprite ul4_1.png"
image sprite_yawn:
        "sprites/sprite ul1.png"
image sprite_hands_on_hips:
        "sprites/sprite ul5.png"
image sprite_in_thoughts2:
        "sprites/sprite ul6.png"
image sprite_something_weird:
        "sprites/sprite ul7.png"

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
        
screen korpus3:
    imagebutton xalign 0.656 yalign 0.175:
        idle ("images/interactive korpus3.png")
        hover ("images/interactive korpus3_aimed.png")
        action Jump("korpus3")
        
screen korpus1:
    imagebutton xalign 0.1726 yalign 0.7156:
        idle ("images/interactive korpus1.png")
        hover ("images/interactive korpus1_aimed.png")
        action Jump("korpus1")
        
screen bloch:
    imagebutton xalign 0.2749 yalign 0.6319:
        idle ("images/interactive bloch.png")
        hover ("images/interactive bloch_aimed.png")
        action Jump("bloch")
        
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
    play music "audio/2song.mp3"
    p "Привет! Рада видеть тебя в нашем университете! Сегодня я буду твоим экскурсоводом. Меня зовут Ульяна! А тебя, значит..?"

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
    
    queue music "audio/jazz.mp3"
    queue music "audio/main v2.mp3"

    show sprite_closed_eye:
        xalign 0.5 yalign 0.3

    e "Сейчас мы находимся в главном холле Кемеровского Государтвенного Университета
    - КемГУ ^-^ Как тебе?"
    
    hide sprite_closed_eye
    show sprite_in_thoughts:
        xalign 0.5 yalign 0.3
    with dissolve
     

    e "Обычно здесь очень людно. Также это место часто преображается в зависимости
    от праздников или посещающих нас гостей."
    e "Выглядит мило, правда? И это только начало. Уже представляешь, что ждёт нас дальше?"
    
    hide sprite_in_thoughts
    show sprite_hands_on_hips
    with dissolve
    e "М-м? Не впечатлило? Ну, тогда я покажу тебе кое-что ещё. Пойдём за мной."
    
    hide hall_1
    
    play sound "audio/walking in a building.mp3"
    
    show library
    with Fade(1.1, 0.5, 1.2)
    
    e "Тсс, не шуми!"
    show sprite_in_thoughts2:
        xalign 0.5 yalign 0.3
    with dissolve
    e "Это библиотека на 2-м этаже. Здесь ты можешь отдохнуть в тишине после
    тяжелого учебного дня. Также тут можно взять необходимую тебе книжку, но не забудь вернуть!"
    #e "Эээ... Нет, здесь нет журналов такого рода..."
    #e "Так, о чем это я? Ах, да. Почитать и отдохнуть."
    hide sprite_in_thoughts2
    show sprite_in_thoughts:
        xalign 0.5 yalign 0.3
    with dissolve
    e "Кстати, это не единственная библиотека в этом корпусе! Спустившись на первый этаж и пройдя
    чуть вдаль по корридору ты сможешь её найти. Но давай посмотрим более жив... интересные места!"
    
    hide library
    
    show zoo
    with dissolve
    
    show sprite_closed_eye
    e "Та-дам!"
    e "Ты, наверное, не думал, что у нас есть свой зоопарк ^-^ "
    hide sprite_closed_eye
    show sprite_in_thoughts2
    with dissolve
    e "Конечно, он не такой большой, как в других зоопарках,
    но всё же помогает студентам немного отвлечься"
    e "Посмотри, какая красота!"
    hide sprite_in_thoughts2
    window hide
    pause
    show sprite_in_thoughts:
            xalign 0.5 yalign 0.3
    with dissolve
    menu:
        e "Тебе нравится?"
        
        "Да":
            main "Ну.."
            hide zoo
            hide sprite_in_thoughts
            show fish
            with dissolve
            e "ДА КОНЕЧНО НРАВИТСЯ! Ты посмотри, какие они все милые uwu"
        "Нет":
            main "Ну.."
            hide zoo
            hide sprite_in_thoughts
            show fish
            with dissolve
            e "ДА КОНЕЧНО НРАВИТСЯ! Ты посмотри, какие они все милые uwu"
    e "Пойдём дальше!"
    
    hide zoo
    
    scene corridor1
    play sound "audio/walking in a building.mp3"
    show corridor1
    with Fade(1.0, 0.5, 1.0)
    
    show sprite_in_thoughts2:
        xalign 0.5 yalign 0.3
    with dissolve
    
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
            "..."
            hide sprite_in_thoughts2
            show sprite_something_weird at left
                #xalign 0.5 yalign 0.3
            with dissolve
            e "Э-ээ. Ну хорошо, но давай всё равно заглянем в столовую."
        "Да, я бы не отказался перекусить." if pol:
            main "Совсем немного..."
            e "Замечательно, я как раз хотела показать тебе столовую! Иди за мной."
    
    hide corridor1
    
    play sound "audio/walking in a building.mp3"
    show food1
    with Fade(1.1, 0.5, 1.2)
    
    show sprite_closed_eye:
        xalign 0.5 yalign 0.3
    e "А вот и столовая!"
    e "Устройся поудобнее, [mainname], а я пока схожу и возьму тебе что-нибудь перекусить."
    hide sprite_closed_eye
    
    "[e] ушла, а я решаю осмотреться."
    "Интерьер выглядит весьма приятно. Интересно, еда здесь такая же на вкус?"
    "..."
    e "Прости, что заставила ждать!"
    
    hide food1
    
    show food1
    with Fade(1.5, 1, 1.5)
    
    show sprite_something_weird at left
    with dissolve
    
    e "Хмм"
    "..."
    hide sprite_something_weird
    show sprite_in_thoughts2:
        xalign 0.5 yalign 0.3
    with dissolve
    e "Думаю, пришло время дать тебе возможность походить самостоятельно."
    e "Сейчас мы придём к нашей главной карте, по которой ты будешь ориентироваться в дальнейшем."
    e "Надеюсь, после этой экскурсии у тебя останутся только приятные впечатления."
    
    hide food1
    
    
    jump map

label map:
    play sound "audio/walking in a building.mp3"
    show map
    with Fade(1.1, 0.5, 1.2)
    
    show screen korpus2
    show screen korpus5
    show screen korpus3
    show screen korpus1
    show screen bloch
    window hide
    pause

label korpus1:
    hide screen korpus2
    hide screen korpus5
    hide screen korpus3
    hide screen korpus1
    hide screen bloch

    play sound "audio/walking in a building.mp3"
    show hall_1
    with Fade(1.1, 0.5, 1.2)

    "Прекрасный первый корпус КемГУ"
    menu:
        "Пойти в столовую":
            hide hall_1
            
            play sound "audio/walking in a building.mp3"
            show food1
            with Fade(1.1, 0.5, 1.2)
            
                            
            "Какие здесь всё-таки красивые столовые."
            "Но, думаю, пора возвращаться."
            
            hide food1
            
            jump korpus1
        "Пойти к блочным аудиториям.":
            hide korpus1
            
            jump bloch
        "Осмотреться":
            hide hall_1
            
            show hall_2
            with fade
            
            "..."
            
            hide hall_2
            
            show hall_3
            with fade
            
            "..."
            
            menu:
                "Пойти в столовую":
                    hide hall_3
            
                    play sound "audio/walking in a building.mp3"
                    show food1
                    with Fade(1.1, 0.5, 1.2)
                
                    "Какие здесь всё-таки красивые столовые."
                    "Но, думаю, пора возвращаться."
                
                    hide food1
                
                    jump korpus1
                "Пойти к блочным аудиториям.":
                    hide hall_3
            
                    jump bloch

label bloch:
    hide screen korpus2
    hide screen korpus5
    hide screen korpus3
    hide screen korpus1
    hide screen bloch

    play sound "audio/walking in a building.mp3"
    show bloch
    with Fade(1.1, 0.5, 1.2)

    "Блочные аудитории."
    "Здесь, в основном, проводятся лекции"
    
    menu:
        "Пойти в первый корпус":
            hide bloch
            
            jump korpus1
        "Вернуться к карте":
            hide bloch
            
            jump map
        "Пойти в пятый корпус":
            hide bloch
            
            jump korpus5

label korpus5:
    hide screen korpus2
    hide screen korpus5
    hide screen korpus3
    hide screen korpus1
    hide screen bloch

    play sound "audio/walking in a building.mp3"
    show korpus5_1
    with Fade(1.1, 0.5, 1.2)
    
    "Прекрасный пятый корпус КемГУ"
    
    menu:
        "Пройти в столовую":
            jump food2
        "Вернуться к карте":
            jump map
        "Пойти во второй корпус":
            hide korpus5_1
            
            jump korpus2_1
    
    return

label food2:
    show food2
    with Fade(1.1, 0.5, 1.2)
    
    "Какие здесь всё-таки красивые столовые"
    "..."
    "Думаю, пора вернуться обратно"
    
    hide food2
    
    jump korpus5
label korpus3:
    hide screen korpus2
    hide screen korpus5
    hide screen korpus3
    hide screen korpus1
    hide screen bloch
    
    play sound "audio/walking in a building.mp3"
    show korpus3
    with Fade(1.1, 0.5, 1.2)

    "Прекрасный третий корпус КемГУ"
    
    return

label korpus2_1:
    hide screen korpus2
    hide screen korpus5
    hide screen korpus3
    hide screen korpus1
    hide screen bloch
    
    play sound "audio/walking in a building.mp3"
    show korpus2_1
    with Fade(1.1, 0.5, 1.2)
    
    "Прекрасный второй корпус КемГУ"
    
    menu:
        "Пойти в пятый корпус":
            hide korpus2_1
            
            jump korpus5
        "Осмотреться":
            hide korpus2_1
            show korpus2_2
            with fade
            "..."
            
            menu:
                "Пойти в пятый корпус":
                    hide korpus2_1
            
                    jump korpus5
                "Пойти к блочным аудиториям":
                    hide korpus2_1
            
                    jump bloch
            
        "Пойти к блочным аудиториям":
            hide korpus2_1
            
            jump bloch
    
    

    #здесь уходят в столовку или куда там надо было

    "здесь кончается пробная версия,
    спасибо за прохождение."

    return