'''
waitress-serve --host 192.168.1.100 --port 7398 temp:app
'''

import requests
import time

API_KEY = "81e52169204e0fa54035388bf5763f59"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"  # Pode usar w780, original, etc.

def buscar_dados_filme(titulo, ano):
    url_search = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": titulo,
        "language": "pt-BR",
        "year": ano
    }

    time.sleep(0.3)  # 300 ms = até 3,3 requisições por segundo
    resposta = requests.get(url_search, params=params)
    if resposta.status_code == 200:
        print(f'Filme \033[33m"{titulo}"\033[0m requsitado',end='')
        dados = resposta.json()

        if dados["results"]:
            print(' com \033[32msucesso\033[0m')
            filme = dados["results"][0]
            movie_id = filme["id"]
            sinopse = filme.get("overview", "Sinopse não encontrada.")
            poster_path = filme.get("poster_path")

            poster_url = f"{IMAGE_BASE_URL}{poster_path}" if poster_path else "Poster não disponível"

            return {
                "titulo": titulo,
                "sinopse": sinopse,
                "poster": poster_url
            }
        else:
            print(' com \033[31mfalha\033[0m')
            return {
                "titulo": titulo,
                "sinopse": "Filme não encontrado.",
                "poster": "nopic.jpg"
            }

def buscar_filmes(lista_de_titulos):
    resultados = []
    for infos in lista_de_titulos:
        if isinstance(infos,list):
            titulo,ano = infos
            dados = buscar_dados_filme(titulo,ano)
        else: dados = infos    
        resultados.append(dados)
    return resultados

filmes = {
    "Arquitrama": buscar_filmes([
        {"titulo": "O GRANDE ROUBO DE TREM",
            "sinopse": "Um dos primeiros filmes produzidos no cinema americano, notável como um dos primeiros filmes que apresentou uma narrativa, que contou uma história. O funcionário da estação de trem é assaltado e deixado amarrado por quatro homens, em seguida, eles roubam o trem ameaçando o operador. Eles roubam todo o dinheiro e atiram num passageiro antes de fugir. Uma menina descobre o funcionário amarrado e avisa ao xerife, que sai junto com seus homens à caça dos bandidos. Algumas cópias do filme tem algumas cenas colorizadas a mão.",
            "poster": "https://image.tmdb.org/t/p/original/vM2vptkSapUFdpaBy7V7jwKy6MA.jpg"
        },
        {"titulo": "OS ÚLTIMOS DIAS DE POMPEIA",
            "sinopse": "Em 79 A.D., o respeitável pompeiano Glaucus tem um ato de generosidade ao comprar Nídia, uma escrava cega que é maltratada por sua dona. Nídia apaixona-se pelo novo mestre, mas ele só tem olhos para Jone. Esta, por sua vez, é cobiçada por Arbace, sacerdote egípcio de Ísis. Quando Nídia implora o auxílio de Isis para conquistar o coração de Glaucus, Arbace dá a ela uma poção de amor que afeta a mente, mas não o coração de Glaucus.",
            "poster": "https://image.tmdb.org/t/p/original/w4HhfyXRV2MLEcbreKJD0V7sUlt.jpg"
        },
        {"titulo": "O GABINETE DO DR. CALIGARI",
            "sinopse": "Num pequeno vilarejo da fronteira holandesa, o misterioso hipnotizador Dr. Caligari (Krauss) chega acompanhado do sonâmbulo Cesare (Veidit), que estaria supostamente adormecido por 23 anos. À noite, Cesare perambula pela cidade concretizando as previsões funestas do seu mestre, o Dr. Caligari.",
            "poster": "https://image.tmdb.org/t/p/original/j09TT0S1crBSYjPu14vgzSSFqFo.jpg"
        },
        {"titulo": "OURO E MALDIÇÃO",
            "sinopse": "O filme mostra a transformação do caráter de três pessoas. Após um bom tempo trabalhando em uma mina, McTeague se muda para a Califórnia, onde passa a trabalhar ilegalmente como dentista, e conhece e se casa com Trina, prima de seu amigo Marcus, também interessado nela. Trina ganha um grande prêmio na loteria e, aos poucos, vai sendo dominada pela avareza, o que desperta o caráter violento de McTeague, e a inveja de Marcus.",
            "poster": "https://image.tmdb.org/t/p/original/eur2vc2BGiOocBuBLVPXySO7lRh.jpg"
        },
        {"titulo": "O ENCOURAÇADO POTEMKIN",
            "sinopse": "Em 1905, na Rússia czarista, aconteceu um levante que pressagiou a Revolução de 1917. Tudo começou no navio de guerra Potemkin quando os marinheiros estavam cansados de serem maltratados, sendo que até carne estragada lhes era dada com o médico de bordo insistindo que ela era perfeitamente comestível. Alguns marinheiros se recusam em comer esta carne, então os oficiais do navio ordenam a execução deles. A tensão aumenta e, gradativamente, a situação sai cada vez mais do controle. Logo depois dos gatilhos serem apertados Vakulinchuk (Aleksandr Antonov), um marinheiro, grita para os soldados e pede para eles pensarem e decidirem se estão com os oficiais ou com os marinheiros. Os soldados hesitam e então abaixam suas armas. Louco de ódio, um oficial tenta agarrar um dos rifles e provoca uma revolta no navio, na qual o marinheiro é morto. Mas isto seria apenas o início de uma grande tragédia.",
            "poster": "https://image.tmdb.org/t/p/original/fV0qRyxd94zai83HeO8MOVQvLmE.jpg"
        },
        {"titulo": "M - O VAMPIRO DE DUSSELDORF",
            "sinopse": "Um assassino de crianças deixa a cidade inteira com medo. A polícia está frenética e desesperadamente procurando por ele, prendendo qualquer um que seja minimamente suspeito. Enquanto isso, os chefes das gangues, furiosos com os ataques que estão sofrendo por causa do assassino, decidem procurá-lo eles mesmos.",
            "poster": "https://image.tmdb.org/t/p/original/626MQmALmMxqV15G8zQMd2K9k45.jpg"
        },
        {"titulo": "O PICOLINO",
            "sinopse": "Um dançarino americano ensaia um número de sapateado em seu quarto de hotel em Londres e acaba incomodando a vizinha do quarto de baixo. Logo ambos começam a se apaixonar. Mas um certo mal-entendido pode colocar tudo a perder...",
            "poster": "https://image.tmdb.org/t/p/original/7we4vnoODrF7dl3AYlrkOkh53vW.jpg"
        },
        {"titulo": "A GRANDE ILUSÃO",
            "sinopse": "A Primeira Guerra Mundial em uma época que ela não era conhecida como tal - o filme conta a história de um grupo de soldados franceses presos em um campo de prisioneiros na Alemanha em 1916, de suas análises sobre a guerra e do comportamento humano no meio dela.",
            "poster": "https://image.tmdb.org/t/p/original/avoVPM51OM4JQUYPE5c950WjuSZ.jpg"
        },
        {"titulo": "LEVADA DA BRECA",
            "sinopse": "Ao tentar garantir uma doação de US $ 1 milhão para seu museu, um paleontólogo confuso é perseguido por uma herdeira volúvel e muitas vezes irritante e seu animal de estimação o leopardo Baby.",
            "poster": "https://image.tmdb.org/t/p/original/2mFEl0iOC6Ci38PRozjDXBLhNFP.jpg"
        },
        {"titulo": "CIDADÃO KANE",
            "sinopse": "Charles Foster Kane foi um menino pobre que acaba se tornando um dos homens mais ricos do mundo. O filme inicia com a sua morte, momentos antes da qual pronuncia a palavra \"Rosebud\". Após dias de sensacionalismo em cima da notícia de sua morte, o jornalista Jerry Thompson é enviado por seu chefe para investigar a vida de Kane, a fim de descobrir o sentido de sua última palavra, a qual ninguém sabia. Entrevistando pessoas do passado de Kane, o jornalista mergulha na vida de um homem solitário, que desde a infância é obrigado a seguir a vontade alheia. Ninguém a seu redor importa-se com Kane, que busca por meio da aquisição de bens a adoração das pessoas. Ao final, Thompson, após a exaustiva investigação da vida de Kane através de entrevistas, se vê incapaz de descobrir o significado da palavra, concluindo que \"Charles Foster Kane foi um homem que possuiu tudo o que quis e depois perdeu tudo. Talvez Rosebud seja algo que ele nunca tenha possuído ou algo que tenha perdido\".",
            "poster": "https://image.tmdb.org/t/p/original/7RdvqkBX2gi6kiZ2yySeRqeClur.jpg"
        },
        {"titulo": "DESENCANTO",
            "sinopse": "Laura (Celia Johnson) e Alec (Trevor Howard) se conhecem por acaso em uma estação de trem, quando ele remove um cisco do olho dela. Ele é um médico, ela é uma dona de casa. Ambos são de classe média, têm meia-idade e são razoavelmente felizes em seus casamentos. Em pouco tempo passam a se encontrar todas as quintas-feiras, mas apenas como bons amigos. Gradativamente surge uma paixão mútua e eles continuam a se encontrar regularmente, apesar de saberem que este amor é impossível.",
            "poster": "https://image.tmdb.org/t/p/original/z02oc9sMEMePtjT0URPDi0GvJIP.jpg"
        },
        {"titulo": "OS SETE SAMURAIS",
            "sinopse": "Um bando de bandidos aterroriza os habitantes de uma pequena cidade, saqueando-os periodicamente sem piedade. Para repelir estes ataques, os aldeões decidem contratar mercenários. Por fim, obtêm os serviços de 7 guerreiros, 7 samurais dispostos a defendê-los em troca apenas de abrigo e comida.",
            "poster": "https://image.tmdb.org/t/p/original/telXEMxGtJvffm5JDsx1rQzwWlf.jpg"
        },
        {"titulo": "MARTY",
            "sinopse": "Marty Piletti é um açougueiro ítalo-americano, tímido e solitário, e que vive no Bronx em Nova Iorque. Ele acredita que nunca nenhuma mulher se interessará por ele mas, por insistência de sua mãe, ele sai uma noite para dançar e conhece uma professora, que se sente tão rejeitada quanto ele. A insegurança dos dois, porém, é um entrave que pode prejudicar a relação deles.",
            "poster": "https://image.tmdb.org/t/p/original/8tnGO5VoAQII4DbE3hozWKhV4BY.jpg"
        },
        {"titulo": "O SÉTIMO SELO",
            "sinopse": "Após dez anos, um cavaleiro retorna das Cruzadas e encontra o país devastado pela Peste Negra. Sua fé em Deus é sensivelmente abalada e, enquanto reflete sobre o significado da vida, a Morte surge à sua frente querendo levá-lo, pois chegou sua hora. Objetivando ganhar tempo, convida-a para um jogo de xadrez que decidirá se ele parte com ela ou não. Tudo depende da sua vitória no jogo e a Morte concorda com o desafio, já que não perde nunca.",
            "poster": "https://image.tmdb.org/t/p/original/j1xE9l5n3Qk0d0pRG0iz9oNNwoH.jpg"
        },
        {"titulo": "DESAFIO À CORRUPÇÃO",
            "sinopse": "Um jogador de bilhar joga contra um campeão em um único jogo de alto risco.",
            "poster": "https://image.tmdb.org/t/p/original/f5MZDPjzyuDfVQInT2CEtFLZfmO.jpg"
        },
        {"titulo": "2001 - UMA ODISSEIA NO ESPAÇO",
            "sinopse": "Desde a “Aurora do Homem” (a pré-história), um misterioso monólito negro parece emitir sinais de outra civilização, assim interferindo no nosso planeta. Quatro milhões de anos depois, no século XXI, uma equipe de astronautas liderados pelo experiente David Bowman e Frank Poole é enviada ao planeta Júpiter para investigar o enigmático monólito na nave Discovery, totalmente controlada pelo computador HAL-9000. Entretanto, no meio da viagem, HAL-9000 entra em pane e tenta assumir o controle da nave, eliminando um a um os tripulantes.",
            "poster": "https://image.tmdb.org/t/p/original/pVCmLuATJ0lQs4Vx1zUJUN0if2A.jpg"
        },
        {"titulo": "O PODEROSO CHEFÃO - PARTE 2",
            "sinopse": "Após a máfia matar sua família, o jovem Vito foge da sua cidade na Sicília e vai para a América. Vito luta para manter sua família. Ele mata Black Hand Fanucci, que exigia dos comerciantes uma parte dos seus ganhos. Com a morte de Fanucci, o poderio de Vito cresce, mas sua família é o que mais importa para ele. Agora baseado no Lago Tahoe, Michael planeja fazer incursões em Las Vegas e Havana instalando negócios ligados ao lazer, mas descobre que aliados como Hyman Roth estão tentando matá-lo.",
            "poster": "https://image.tmdb.org/t/p/original/7g6wvsWHxBQujUcSXvZLhdFpDUy.jpg"
        },
        {"titulo": "DONA FLOR E SEUS 2 MARIDOS",
            "sinopse": "A minissérie de 20 episódios editada como um telefilme de 141 minutos em comemoração aos 50 anos da TV Globo. A bela e prendada Flor se casa com o envolvente Vadinho, mas logo descobre que o marido é um malandro que a engana, colecionando amantes e dívidas por toda a cidade de Salvador. Vadinho morre inesperadamente durante uma farra de carnaval e a desamparada Flor acaba se casando com o farmacêutico Teodoro, que é o oposto de seu finado ex marido.",
            "poster": "https://image.tmdb.org/t/p/original/g9vR6svpQdQjLrPp3METrHHUYQZ.jpg"
        },
        {"titulo": "UM PEIXE CHAMADO WANDA",
            "sinopse": "Com o intuito de seduzir Archie para descobrir o esconderijo das jóias roubadas por um de seus clientes, Wanda está pronta para agir! Infelizmente para ambos, o namorado e parceiro da moça (Kline) também está pronto para agir, mas contra Archie! Quem ficará com as jóias? Quem ficará com Wanda? Fica aqui o suspense, mas uma coisa é certa: \"Um Peixe Chamado Wanda\" é um filme que com certeza vai fisgar você!",
            "poster": "https://image.tmdb.org/t/p/original/qHoIjKdJzlbvUwk4G55AtIem2rG.jpg"
        },
        {"titulo": "QUERO SER GRANDE",
            "sinopse": "Em um passeio num parque de diversões Josh acaba barrado na montanha-russa. Revoltado, ele pede à máquina dos desejos para ser grande. No dia seguinte o pedido foi realizado e a mãe o expulsa de casa, pois não conhece aquele estranho de trinta anos. Josh, porém, continua sendo apenas uma criança e agora precisa aprender a se relacionar no mundo dos adultos.",
            "poster": "https://image.tmdb.org/t/p/original/vJgc36oSlup6uhWoXURB6d4Gyd8.jpg"
        },
        {"titulo": "AMOR E SEDUÇÃO",
            "sinopse": "Na China rural dos anos 1920, jovem camponesa é forçada a casar-se com velho dono de fábrica e inicia um romance com o sobrinho do marido, levando a um trágico desfecho.",
            "poster": "https://image.tmdb.org/t/p/original/ejvX1lukPZZ10jatUWmKaXbhjGI.jpg"
        },
        {"titulo": "THELMA & LOUISE",
            "sinopse": "Louise Sawyer (Susan Sarandon) é uma garçonete quarentona e Thelma (Geena Davis) é uma jovem dona de casa. Cansadas da vida monótona que levam, as amigas resolvem deixar tudo para trás e pegar a estrada. Durante a viagem, elas se envolvem em um crime e decidem fugir para o México, mas acabam sendo perseguidas pela polícia americana.",
            "poster": "https://image.tmdb.org/t/p/original/y66rxathLobXk7xaUgPr4etBkRN.jpg"
        },
        {"titulo": "QUATRO CASAMENTOS E UM FUNERAL",
            "sinopse": "Charles (Hugh Grant) é um solteirão que nunca quis nada sério com ninguém, até conhecer uma envolvente mulher, por quem se apaixona. Sua complicada situação de assumir relacionamentos pode mudar depois de três outros casamentos e um funeral, que dão título ao longa.",
            "poster": "https://image.tmdb.org/t/p/original/45SnCikWqQVCK3LZbUMtqwusqpW.jpg"
        },
        {"titulo": "SHINE - BRILHANTE",
            "sinopse": "Numa noite de inverno David entre num bar. Embora claramente excêntrico, ele é um excelente pianista, despertando desde logo a atenção e a simpatia de todos. A sua vida sempre foi caracterizada pelo domínio avassalador do seu pai que sempre pretendeu transformá-lo num grande pianista apesar do seu excessivo protecionismo. Desafiando a autoridade do seu pai, aceita um convite para ir estudar para Londres. Apesar de toda a sua genialidade David tem bastantes dificuldades de adaptação o que transforma sua vida num caos.",
            "poster": "https://image.tmdb.org/t/p/original/cbmThowj2XAW7lKlMAXmnhZvjGI.jpg"
        }
    ]),
    "Minitrama": buscar_filmes([
        {"titulo": "NANOOK, O ESQUIMÓ",
            "sinopse": "O antropólogo Robert Flaherty, com sua câmera rudimentar, decide filmar a vida e os costumes dos esquimós de Port Huron, perto da Baía de Hudson, no Canadá.",
            "poster": "https://image.tmdb.org/t/p/original/9WAboi1QbKu41WkyGxQVNpXwwxx.jpg"
        },
        {"titulo": "A PAIXÃO DE JOANA D'ARC",
            "sinopse": "França, século XV, Joana de Domrémy, filha do povo, resiste bravamente a ocupação de seu país. É presa, humilhada, torturada e interrogada de maneira impiedosa por um tribunal eclesiástico, que a levou, involuntariamente, a blasfemar.",
            "poster": "https://image.tmdb.org/t/p/original/apW5bhsxn9fai3ZMpC4l03lhhdo.jpg"
        },
        {"titulo": "ZERO DE COMPORTAMENTO",
            "sinopse": "Volta aos tempos de escola num colégio do interior, as bagunças dentro do dormitório, a punição severa, a recreação, o estudo indisciplinado e os confrontos com a administração. Um noite os garotos internos decidem se libertar da autoridade dos adultos e uma revolta arrebenta. Esta é a obra mais autobiográfica de Jean Vigo.",
            "poster": "https://image.tmdb.org/t/p/original/5o8bj4JyxaNFE81NLjcVgrqWtsp.jpg"
        },
        {"titulo": "PAISÁ",
            "sinopse": "\"Paisà\" retrata, em 6 episódios, a progressão das tropas americanas de libertação, desde o desembarque na Sicília até aos pântanos do vale do rio Pó. A descrição da realidade imediata, na linha de \"Roma Città Aperta\", a utilização de não profissionais, o aspecto de documentário da fotografia, tudo faz de \"Paisà\" uma obra em completa ruptura com o cinema italiano da década anterior.  - Uma mulher leva uma patrulha aliada através de um campo de minas. Ela morre protegendo um GI, mas os ianques acham que ela o matou.  - Um menino de rua rouba os sapatos de um GI.  - Um GI conhece uma mulher no dia que Roma é libertada. 6 meses depois eles se reencontram. Ele é um cínico, ela é uma prostituta.  - Uma enfermeira americana se arrisca cruzar o rio Arno, em meio ao fogo alemão, em busca do Partisan que ama.  - 3 capelães, incluindo um judeu, se abrigam num mosteiro ao norte dos Apeninos.  - Soldados aliados e partisans tentam escapar pelos pântanos do rio Pó.",
            "poster": "https://image.tmdb.org/t/p/original/dbe6wuhiMU9XXzdnmYZinKnRSZS.jpg"
        },
        {"titulo": "MORANGOS SILVESTRES",
            "sinopse": "O rabugento médico aposentado Isak Borg viaja de Estocolmo para Lund, na Suécia, com sua nora grávida e infeliz, Marianne, para receber um diploma honorário da universidade onde estudou. Ao longo do caminho, eles cruzam com uma série de caroneiros, cada um deles fazendo com que o médico idoso reflita sobre os prazeres e as falhas de sua própria vida, incluindo a vivaz jovem Sara, que se parece muito com o próprio primeiro amor do médico.",
            "poster": "https://image.tmdb.org/t/p/original/7VxdomQ3siOTDSDFwFhMw8vDSSw.jpg"
        },
        {"titulo": "A SALA DE MÚSICA",
            "sinopse": "O último representante de uma alta casta insiste em manter o padrão de vida de seus antepassados, mesmo vivendo uma situação cada vez mais difícil. Uma das coisas da qual não abre mão é a enorme sala de música de sua mansão. Seu amor à música e seus atos acabam levando sua família à ruína.",
            "poster": "https://image.tmdb.org/t/p/original/21Mfk2TTrgy2rv4jeINMKRUUdhW.jpg"
        },
        {"titulo": "O DESERTO VERMELHO",
            "sinopse": "Chuva, neblina, frio e poluição assolam a cidade industrial de Ravenna, na Itália. Ugo, o gerente de uma usina local, é casado com Giuliana, uma dona de casa que sofre de problemas psicológicos. Um dia, ela conhece o engenheiro Zeller, o que pode mudar sua vida. Em O Deserto Vermelho, Antonioni, no auge de sua forma, aborda os temas centrais de sua filmografia: a incomunicabilidade e a solidão do homem contemporâneo.",
            "poster": "https://image.tmdb.org/t/p/original/86GAyXEo1nn99wSPIst8e1bsE10.jpg"
        },
        {"titulo": "CADA UM VIVE COMO QUER",
            "sinopse": "Uma desiludido da classe alta Americana pega trabalhos por aí em plataformas de petróleo. Isso quando sua vida não é gasta em uma sucessão miserável de bares, motéis e outros muquifos.  Robert Eroica Dupea (Jack Nicholson) é um ex-pianista clássico que rejeita seu modo de viver, passando a trocar constantemente de mulher e emprego. Robert retorna para casa com Rayette Dipesto (Karen Black), sua namorada, depois de descobrir que seu pai está à beira da morte. Lá, ele conhece Catherine Van Ost (Susan Anspach), uma interessante mulher que o faz ficar dividido. Recebeu 4 indicações ao Oscar: Filme, Ator (Jack Nicholson), Atriz (Karen Black) e Roteiro Original.",
            "poster": "https://image.tmdb.org/t/p/original/6GSX364msRheDR8KyA3UIxCWzOO.jpg"
        },
        {"titulo": "O JOELHO DE CLAIRE",
            "sinopse": "“Por que me prenderia a uma mulher se outras ainda me interessassem?” São essas as palavras de Jerôme enquanto planeja se casar com a filha de um diplomata no fim do verão. Até lá, ele passa seus dias em uma pensão à beira do lago, paquerando Laura, de 16 anos, e sua meia-irmã loira, Claire.",
            "poster": "https://image.tmdb.org/t/p/original/rn8iSGBu4jI3r8NUZa8s8Und7JF.jpg"
        },
        {"titulo": "O IMPÉRIO DOS SENTIDOS",
            "sinopse": "A história de uma ex-prostituta que envolve-se em um caso de amor obsessivo com o senhorio de uma propriedade onde ela trabalha como criada. O que começa como uma diversão inconseqüente transforma-se em uma paixão que ultrapassa quaisquer limites.",
            "poster": "https://image.tmdb.org/t/p/original/28XPd5gYMQ418PxfLybfAxw5zYI.jpg"
        },
        {"titulo": "A FORÇA DO CARINHO",
            "sinopse": "Mac Sledge (Robert Duvall) é um cantor de músicas country que guarda amargas recordações de sua vida. Com sua carreira em declínio, ele se entrega de vez à bebida. Até que, num hotel do Texas, conhece Rosa Lee (Tess Harper), uma viúva com um filho de 10 anos. Logo Rosa e Mac iniciam um relacionamento, que o faz recuperar a alegria de viver.",
            "poster": "https://image.tmdb.org/t/p/original/kZsRcsmQhs3SZ20ZuQLjLp41qLd.jpg"
        },
        {"titulo": "PARIS, TEXAS",
            "sinopse": "Um homem sai do deserto sem lembranças de sua vida passada e é apenas com a ajuda de seu irmão que ele percebe que abandonou sua esposa e seu filho quatro anos antes.",
            "poster": "https://image.tmdb.org/t/p/original/i9CQ0biql97FgyICpQ5uIwbh7GE.jpg"
        },
        {"titulo": "O SACRIFÍCIO",
            "sinopse": "No dia de seu aniversário, enquanto comemora com sua família, Alexander e todos recebem através da televisão uma notícia inesperada: a Terceira Guerra Mundial, e consequentemente um holocausto nuclear haviam começado. Em desespero, mesmo tendo antes revelado não sentir mais fé em Deus, Alexander implora aos céus que aquilo não aconteça, e oferece tudo o que tem para que um milagre afaste o horror da guerra.",
            "poster": "https://image.tmdb.org/t/p/original/2xjJwPhmut83eBV75rUNfGZ5pgr.jpg"
        },
        {"titulo": "PELLE, O CONQUISTADOR",
            "sinopse": "No final do século XIX, dois emigrantes suecos, Lasse Karlsson e seu filho Pelle, chegam à ilha dinamarquesa de Bornholm na esperança de encontrar trabalho em uma fazenda e poupar dinheiro suficiente para viajar para os Estados Unidos da América.",
            "poster": "https://image.tmdb.org/t/p/original/oSsu4khg459yTR1sw4qjEC4LO5J.jpg"
        },
        {"titulo": "IL LADRO DI BAMBINI",
            "sinopse": "Antonio, a policeman (carabiniere), has an order to take two children (Rosetta and her brother Luciano) from Milan to Sicily to an orphanage. Their mother has been arrested for forcing Rosetta (11 years old) to work as a prostitute. First the relation between Antonio and the children is tough, but it relaxes so they become temporary friends.",
            "poster": "https://image.tmdb.org/t/p/original/fkFYNR4iCz5n1j5Drf0jejKmNVb.jpg"
        },
        {"titulo": "NADA É PARA SEMPRE",
            "sinopse": "O filme é baseado na novela homônima de Norman MacLean e narra a verdadeira história de dois jovens Norman e Paul que cresceram pescando trutas em Montana. Um deles é revoltado com o pai, o Reverendo MacLean, enquanto o outro tem seus pés no chão. A família vive várias aventuras, os irmãos seguem cada um seu caminho, mas alguma coisa os faz retornar sempre à pescaria. Afinal, o rio parece ter algo a dizer aos MacLean.",
            "poster": "https://image.tmdb.org/t/p/original/6Pc791iaMjMxqqu81R9k6AqzerF.jpg"
        },
        {"titulo": "TO LIVE",
            "sinopse": "An undercover cop finds himself tortured by his life among the triads. He’s locked into his job with no way out, and he’s starting to find the triad guys more honorable than his supremely despicable superior officer.",
            "poster": "https://image.tmdb.org/t/p/original/74ATnufP8KcNI8o5JzfdNXecZ8s.jpg"
        },
        {"titulo": "DANÇA COMIGO",
            "sinopse": "Um entediado contador japonês vê uma linda mulher na janela de um estúdio de dança de salão. Ele secretamente começa a ter aulas de dança para ficar perto dela e, com o tempo, descobre o quanto adora dança de salão. Enquanto isso, sua esposa contratou um detetive particular para descobrir por que ele começou a chegar tarde em casa cheirando perfume.",
            "poster": "https://image.tmdb.org/t/p/original/a3HQNANsAZ3zhKpHeWdznwBmJPF.jpg"
        },
        {"titulo": "WELFARE",
            "sinopse": "WELFARE shows the nature and complexity of the welfare system in sequences illustrating the staggering diversity of problems that constitute welfare: housing, unemployment, divorce, medical and psychiatric problems, abandoned and abused children, and the elderly. These issues are presented in a context where welfare workers as well as clients struggle to cope with and interpret the laws and regulations that govern their work and life.",
            "poster": "https://image.tmdb.org/t/p/original/1eFgNI93rRSOFZZ9cajF3tMmGPc.jpg"
        }
    ]),
    "Antitrama": buscar_filmes([
        {"titulo": "UM CÃO ANDALUZ",
            "sinopse": "Sonho? Realidade? Subconsciente? Uma aventura surrealista de Luis Buñuel e Salvador Dalí.",
            "poster": "https://image.tmdb.org/t/p/original/gXLF8fbCrpGZ09bihV7XpYfYG9w.jpg"
        },
        {"titulo": "O SANGUE DE UM POETA",
            "sinopse": "Um artista sem nome é transportado através de um espelho para outra dimensão, onde ele viaja através de diversos cenários bizarros. História contada em quatro episódios.",
            "poster": "https://image.tmdb.org/t/p/original/fgPIIJqrmsmmv23y79rqTMFDm5z.jpg"
        },
        {"titulo": "MESHES OF THE AFTERNOON",
            "sinopse": "Maya Deren é uma mulher aprisionada dentro de casa, sufocada pelo cotidiano doméstico. Ela é atormentada por múltiplas visões, se despedaça em diferentes personalidades, e não consegue diferenciar muito bem, enquanto cochila, o sonho da realidade. Seu olhar para por longos segundos em qualquer objeto doméstico: uma faca em cima do pão, a porta destrancada, o telefone fora do gancho.",
            "poster": "https://image.tmdb.org/t/p/original/zGFxZcMYzwTzw6ViqevL57n808Q.jpg"
        },
        {"titulo": "THE RUNNING JUMPING & STANDING STILL FILM",
            "sinopse": "A short film without any direct action designed more as an experiment, with disjointed comic scenes with no common thread.",
            "poster": "https://image.tmdb.org/t/p/original/i63PTdHuLtjHxcTzs8j2Lvypv22.jpg"
        },
        {"titulo": "ANO PASSADO EM MARIENBAD",
            "sinopse": "No luxuoso hotel, um estranho tenta convencer uma mulher casada a fugir com ele, alegando que ambos haviam tido um caso amoroso no ano anterior, em Marienbad. Mas a mulher não se lembra do relacionamento.",
            "poster": "https://image.tmdb.org/t/p/original/tizZ7JnXRFMvoNegu2CtM2ab9E7.jpg"
        },
        {"titulo": "8 1/2",
            "sinopse": "Prestes a rodar sua próxima obra, o cineasta Guido Anselmi (Marcello Mastroianni) ainda não tem idéia de como será o filme. Mergulhado em uma crise existencial e pressionado pelo produtor, pela mulher, pela amante e pelos amigos, ele se interna em uma estação de águas e passa a misturar o passado com o presente, ficção com realidade.",
            "poster": "https://image.tmdb.org/t/p/original/nQkrZRxnvrkb6BV7ZYmdwJoFGDt.jpg"
        },
        {"titulo": "PERSONA QUANDO DUAS MULHERES PECAM",
            "sinopse": "Uma atriz teatral de sucesso sofre uma crise emocional e para de falar. Uma enfermeira é designada a cuidar dela em uma casa reclusa, perto da praia, onde as duas permanecem sozinhas. Para quebrar o silêncio, a enfermeira começa a falar incessantemente, narrando diversos episódios relevantes de sua vida, mas quando descobre que a atriz usa seus depoimentos como fonte de análise, a cumplicidade entre as duas se transforma em embate.",
            "poster": "https://image.tmdb.org/t/p/original/mAE4uwrXLlzo5AAxEorFvErdumq.jpg"
        },
        {"titulo": "WEEKEND À FRANCESA",
            "sinopse": "Um fim de semana supostamente idílico de uma viagem para o campo se transforma em um pesadelo sem fim de engarrafamentos, revolução, canibalismo e assassinato, quando a sociedade burguesa francesa começa a desmoronar sob o peso de suas próprias preocupações como consumidores.",
            "poster": "https://image.tmdb.org/t/p/original/e9p8VdsAKXz1GoVXD36Lg5e3YKo.jpg"
        },
        {"titulo": "DEATH BY HANGING",
            "sinopse": "Um coreano é condenado à morte no Japão, mas de alguma forma sobrevive à sua execução, deixando as autoridades em pânico sobre o que fazer em seguida.",
            "poster": "https://image.tmdb.org/t/p/original/3fRfWloL3al11YnU2tekonTa3JM.jpg"
        },
        {"titulo": "OS PALHAÇOS",
            "sinopse": "Um menino observa um circo ser construído do lado de fora da janela de seu quarto. Assim começa a \"docu-comédia\" de Federico Fellini, uma ode pessoal a uma de suas grandes obsessões.",
            "poster": "https://image.tmdb.org/t/p/original/obL37ec9p87eRpnP5tJuWZSYcTT.jpg"
        },
        {"titulo": "MONTY PYTHON EM BUSCA DO CÁLICE SAGRADO",
            "sinopse": "O Rei Artur sai à procura de cavaleiros que o acompanhe em uma atabalhoada jornada histórica: A busca do Santo Graal. Aparecem então Sir Lancelot, o Bravo; Sir Robin, o Não-Tão-Bravo-Quanto-Sir-Lancelot; Sir Galahad, o Puro, entre outros personagens surreais. Escrita pelo genial grupo de comédia britânico Monty Python, a trama do longa satiriza diversos eventos históricos ocorridos na Idade Média.",
            "poster": "https://image.tmdb.org/t/p/original/hWx1ANiWEWWyzKPN0us35HCGnhQ.jpg"
        },
        {"titulo": "ESSE OBSCURO OBJETO DE DESEJO",
            "sinopse": "Mathieu, francês sofisticado, rico e de meia idade, apaixona-se perdidamente por sua ex-arrumadeira Conchita, bela espanhola de apenas dezenove anos. Começa então um jogo de gato-e-rato surrealista, de fundo sexual, em que Marhieu tenta por todos os meios conquistar os favores de Conchita, enquanto ela o manipula impiedosamente. O objetivo de cada um, desnecessário dizer, é conseguir total controle sobre o outro.",
            "poster": "https://image.tmdb.org/t/p/original/9iUdC4dftkjYSBUJq5DAxC6WqB9.jpg"
        },
        {"titulo": "BAD TIMING",
            "sinopse": "Alex Linden is a psychiatrist living in Vienna who meets Milena Flaherty though a mutual friend. Though Alex is quite a bit older than Milena, he's attracted to her young, carefree spirit. Despite the fact that Milena is already married, their friendship quickly turns into a deeply passionate love affair that threatens to overtake them both. When Milena ends up in the hospital from an overdose, Alex is taken into custody by Inspector Netusil.",
            "poster": "https://image.tmdb.org/t/p/original/raLS93dykOabizFuguWZ9KeCKAS.jpg"
        },
        {"titulo": "ESTRANHOS NO PARAÍSO",
            "sinopse": "O preguiçoso nova-iorquino Willie cria um vínculo inesperado com sua jovem prima húngara Eva quando ela faz uma visita surpresa. Mais tarde, Eva vai morar com sua tia em Cleveland, e Willie leva seu melhor amigo Eddie para visitá-la, resultando em uma viagem estranha e agitada até a Flórida.",
            "poster": "https://image.tmdb.org/t/p/original/A4YPanjmXCQT6SZNo6AQSoUxkLZ.jpg"
        },
        {"titulo": "DEPOIS DE HORAS",
            "sinopse": "Em um café de Manhattan, o processador de texto Paul Hackett se reúne e fala de literatura com Marcy. Mais tarde naquela noite, Paul pega um táxi para o apartamento de Marcy no centro da cidade. Sua nota de 20 dólares voa para fora da janela durante a corrida anunciando a noite inesperada que ele terá. Ele não pode pagar pela corrida e encontra-se em uma série de situações embaraçosas e com risco de morte.",
            "poster": "https://image.tmdb.org/t/p/original/eamOBurHBu0MIxohTIVcfxmZ6Z7.jpg"
        },
        {"titulo": "ZOO - UM Z E DOIS ZEROS",
            "sinopse": "Um carro colide com um cisne do lado de fora do zoológico de Roterdã. Duas passageiras morrem e a motorista, Alma, tem sua perna amputada. Obcecados pelo acidente, os maridos das mulheres mortas – gêmeos – iniciam um estranho caso com Alma.",
            "poster": "https://image.tmdb.org/t/p/original/jUjZjKaluqfiVMUTrNctASbqA7X.jpg"
        },
        {"titulo": "QUANTO MAIS IDIOTA MELHOR",
            "sinopse": "Os metaleiros Wayne e Garth são dois grandes amigos que produzem, diretamente do porão de Wayne, um programa de TV alternativo chamado \"O Mundo de Wayne\", transmitindo-o para uma rede de televisão local. O programa chama a atenção de um executivo de uma grande rede nacional de TV, que tem o interesse de fazer uma versão de alto orçamento do programa para todo o país. Além de lutar para salvar o seu show, Wayne precisa ainda reconquistar sua namorada.",
            "poster": "https://image.tmdb.org/t/p/original/k16ElHcFAHT37C7GpSTue06rh5A.jpg"
        },
        {"titulo": "AMORES EXPRESSOS",
            "sinopse": "Em Hong Kong, dois policiais se apaixonam por duas mulheres muito diferentes: um por uma mulher sedutora e criminosa, o outro, por uma garçonete peculiar.",
            "poster": "https://image.tmdb.org/t/p/original/43I9DcNoCzpyzK8JCkJYpHqHqGG.jpg"
        },
        {"titulo": "ESTRADA PERDIDA",
            "sinopse": "Fred Madison (Bill Pullman) é acusado, sob misteriosas circunstâncias, de matar sua esposa Renee (Patricia Arquette). Ele logo se vê transformado em um outro homem, Pete Dayton (Balthazar Getty), possuindo uma vida completamente diferente. Quando Pete é solto no seu corpo e na sua mente, as coisas ficam cada vez mais misteriosas e intrigantes.",
            "poster": "https://image.tmdb.org/t/p/original/fdTtij6H0sX9AzIjUeynh5zbfm7.jpg"
        },
        {"titulo": "NOITE E NEBLINA",
            "sinopse": "Este documento arrepiante sobre os horrores do Holocausto, filmado apenas dez anos após a libertação dos campos de concentração dirigidos pelos nazistas, usa imagens e imagens de guerra dos campos agora vazios.",
            "poster": "https://image.tmdb.org/t/p/original/7STuJfkpchvlh8v6jVr5ILs5KQB.jpg"
        },
        {"titulo": "KOYAANISQATSI - UMA VIDA FORA DE EQUILÍBRIO",
            "sinopse": "Koyaanisqatsi - Uma Vida Fora de Equilíbrio. As relações entre os seres humanos, a natureza, o tempo e a tecnologia. Cidade, campo, paisagem, rotina, pessoas, construções, destruição. Um documentário sem atores e sem diálogos, composto por uma impressionante coleção de imagens e uma marcante trilha sonora.",
            "poster": "https://image.tmdb.org/t/p/original/6zCNciRcob8lwuydVXgq0esla8L.jpg"
        }
    ]),
    "Outros": buscar_filmes([
        {"titulo": "O Turista Acidental",
            "sinopse": "Onde encontrar seu restaurante de fast-food favorito em Paris? Quantos pacotes de sabão em pó são necessários em uma viagem para Atlanta? Pergunte a Macon Leary, cujos guias de viagem são reverenciados pelos amantes de viagem caseiros, que odeiam estar em trânsito. Sobre as questões do coração, não pergunte a Macon. Ele não tem a menor noção. Pelo menos, não ainda.",
            "poster": "https://image.tmdb.org/t/p/original/dyk2BqPajLRBpVQ6jsSJJdgfuXe.jpg"
        }
    ])
}

# from json import dumps
# print(f'\n\033[34m{dumps(filmes,ensure_ascii=False)}\033[0m\n')

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
def home():
    return f'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Galeria de Filmes</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #111;
            color: #fff;
            padding: 20px;
        }}

        .movie-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
        }}

        .movie {{
            text-align: center;
            cursor: pointer;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 10px;
            background-color: #222;
            transition: transform 0.2s ease;
        }}

        .movie:hover {{
            transform: scale(1.03);
        }}

        .movie img {{
            width: 100%;
            border-radius: 8px;
        }}

        .title {{
            margin-top: 10px;
            font-weight: bold;
            font-size: 1.1em;
        }}

        .details {{
            display: none;
            text-align: left;
            margin-top: 10px;
        }}

        .details img {{
            width: 100%;
            margin-top: 10px;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    {''.join([f"""
    <h2>{tipo}</h2>

    <div class="movie-grid">"""+
        ''.join([f"""
            <div class="movie" onclick="toggleDetails(this)">
                <img src="{filme['poster']}" alt="Filme 1">
                <div class="title">{filme['titulo']}</div>
                <div class="details">
                    <p>{filme['sinopse']}</p>
                </div>
            </div>
        """ for filme in lista])+'</div>' for tipo, lista in filmes.items()])}

    <script>
        function toggleDetails(element) {{
            const details = element.querySelector('.details');
            details.style.display = details.style.display === 'block' ? 'none' : 'block';
        }}
    </script>

</body>
</html>
    '''

# if __name__ == '__main__':
#     app.run(port=7398)#, debug=True)

open('index.html','w',encoding='utf-8').write(home())
