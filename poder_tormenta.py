import inquirer
from inquirer import errors

anatomia_insana = {
    "formatted_name": "anatomia_insana",
    "description": "Você tem 25% de chance (resultado “1” em 1d4) de ignorar o dano adicional de um acerto crítico ou ataque furtivo. A chance aumenta em +25% para cada dois outros poderes da Tormenta que você possui.",
    "name": "Anatomia Insana",
    "requirements": {}
}

antenas = {
    "formatted_name": "antenas",
    "description": "Você recebe +1 em Iniciativa, Percepção e Vontade. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Antenas",
    "increase_expertise": ["iniciativa", "percepcao", "vontade"],
    "requirements": {}
}

armamento_aberrante = {
    "formatted_name": "armamento_aberrante",
    "description": "Você pode gastar uma ação de movimento e 1 PM para produzir uma versão orgânica de qualquer arma corpo a corpo ou de arremesso com a qual seja proficiente — ela brota do seu braço, ombro ou costas como uma planta grotesca e então se desprende. O dano da arma aumenta em um passo  para cada dois outros poderes da Tormenta que você possui. A arma dura pela cena, então se desfaz numa poça de gosma.",
    "name": "Armamento Aberrante",
    "requirements": {
        "power": {
            "tormenta": {
                "quantity": 1
            }
        }
    }
}

articulacoes_flexiveis = {
    "formatted_name": "articulacoes_flexiveis",
    "description": "Você recebe +1 em Acrobacia, Furtividade e Reflexos. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Articulações Flexíveis",
    "requirements": {},
    "increase_expertise": ["acrobacia", "furtividade", "reflexos"]
}

asas_insetoides = {
    "formatted_name": "asas_insetoides",
    "description": "Você pode gastar 1 PM para receber deslocamento de voo 9m até o fim do seu turno. O deslocamento aumenta em +1,5m para cada outro poder da Tormenta que você possui.",
    "name": "Asas Insetoides",
    "requirements": {
        "power": {
            "tormenta": {
                "quantity": 4
            }
        }
    }
}

carapaca = {
    "formatted_name": "carapaca",
    "description": "Sua pele é recoberta por placas quitinosas. Você recebe +1 na Defesa. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "increase_defense": 1,
    "name": "Carapaça",
    "requirements": {}
}

corpo_aberrante = {
    "formatted_name": "corpo_aberrante",
    "description": "Crostas vermelhas em várias partes de seu corpo tornam seus ataques mais perigosos. Seu dano desarmado aumenta em um passo, mais um  passo para cada quatro outros poderes da Tormenta que você possui.",
    "name": "Corpo Aberrante",
    "requirements": {
        "power": {
            "tormenta": {
                "quantity": 1
            }
        }
    }
}

cuspir_enxame = {
    "formatted_name": "cuspir_enxame",
    "description": "Você pode gastar uma ação completa e 2 PM para criar um enxame de insetos rubros em um ponto a sua escolha em alcance curto e com duração sustentada. O enxame tem tamanho Médio e pode passar pelo espaço de outras criaturas. Uma vez por rodada, você pode gastar uma ação de movimento para mover o enxame 9m. No final do seu turno, o enxame causa 2d6 pontos de dano de ácido a qualquer criatura no espaço que ele estiver ocupando. Para cada dois outros poderes da Tormenta que possui, você pode gastar +1 PM quando usa este poder para aumentar o dano do enxame em +1d6.",
    "requirements": {},
    "name": "Cuspir Enxame"

}

dentes_afiados = {
    "formatted_name": "dentes_afiados",
    "description": "Você recebe uma arma natural de mordida (dano 1d4, crítico x2, corte). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida",
    "name": "Dentes Afiados",
    "requirements": {}
}

desprezar_realidade = {
    "formatted_name": "desprezar_realidade",
    "description": "Você pode gastar 2 PM para ficar no limiar da realidade até o início de seu próximo turno. Nesse estado, você ignora terreno difícil e causa 20% de chance de falha em efeitos usados contra você (não apenas ataques). Para cada dois outros poderes de Tormenta que você possuir, essa chance aumenta em 5% (máximo de 50%).",
    "name": "Desprezar a Realidade",
    "requirements": {}
}

empunhadura_rubra = {
    "formatted_name": "empunhadura_rubra",
    "description": "Você pode gastar 1 PM para cobrir suas mãos com uma carapaça rubra. Até o final da cena, você recebe +1 em Luta. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Empunhadura Rubra",
    "requirements": {}
}

fome_mana = {
    "formatted_name": "fome_mana",
    "description": "Quando passa em um teste de resistência para resistir a uma habilidade mágica, você recebe 1 PM temporário cumulativo. Você pode ganhar um máximo de PM temporários por cena desta forma igual ao número de poderes da Tormenta que possui.",
    "name": "Fome de Mana",
    "requirements": {}
}

larva_explosiva = {
    "formatted_name": "larva_explosiva",
    "description": "Se uma criatura que tenha sofrido dano de sua mordida nesta cena for reduzida a 0 ou menos PV, ela explode em chuva cáustica, morrendo e causando 4d4 pontos de dano de ácido em criaturas adjacentes. Para cada dois outros poderes da Tormenta que você possui, o dano aumenta em +2d4. Você é imune a esse dano",
    "name": "Larva Explosiva",
    "requirements": {
        "power": {
            "tormenta": {
                "items": ["dentes_afiados"]
            }
        }
    }
}

legiao_aberrante = {
    "formatted_name": "legiao_aberrante",
    "description": "Seu corpo se transforma em uma massa de insetos rubros. Você pode atravessar qualquer espaço por onde seja possível passar uma moeda (mas considera esses espaços como terreno difícil) e recebe +1 em testes contra manobras de combate e de resistência contra efeitos que tenham você como alvo (mas não efeitos de área). Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Legião Aberrante",
    "requirements": {
        "power": {
            "tormenta": {
                "items": ["anatomia_insana"],
                "quantity": 3
            }
        }

    }
}

maos_membranosas = {
    "formatted_name": "maos_membranosas",
    "description": "Você recebe +1 em Atletismo, Fortitude e testes de agarrar. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Mãos Membranosas",
    "requirements": {},
    "increase_expertise": ["atletismo", "fortitude"]
}

membros_estendidos = {
    "formatted_name": "membros_estendidos",
    "description": "Seus braços e armas naturais são grotescamente mais longos que o normal, o que aumenta seu alcance natural para ataques corpo a corpo  em +1,5m. Para cada quatro outros poderes da Tormenta que você possui, esse alcance aumenta em +1,5m.",
    "name": "Membros Estendidos",
    "requirements": {}
}

membros_extras = {
    "formatted_name": "membros_extras",
    "description": "Você possui duas armas naturais de patas insetoides que saem de suas costas, ombros ou flancos. Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 2 PM para fazer um ataque corpo a corpo extra com cada uma (dano 1d4, crítico x2, corte). Se possuir Ambidestria ou Estilo de Duas Armas, pode empunhar armas leves em suas patas insetoides (mas ainda precisa pagar 2 PM para atacar com elas e sofre a penalidade de –2 em todos os ataques).",
    "name": "Membros Extras",
    "requirements":  {
        "power": {
            "tormenta": {
                "quantity": 4
            }
        }
    }

}

mente_aberrante = {
    "formatted_name": "mente_aberrante",
    "description": "Você recebe resistência a efeitos mentais +1. Além disso, sempre que precisa fazer um teste de Vontade para resistir a uma habilidade, a criatura que usou essa habilidade sofre 1d6 pontos de dano psíquico. Para cada dois outros poderes da Tormenta que você possui o bônus em testes de resistência aumenta em +1 e o dano aumenta em +1d6.",
    "name": "Mente Aberrante",
    "requirements": {}
}

olhos_vermelhos = {
    "formatted_name": "olhos_vermelhos",
    "description": "Você recebe visão no escuro e +1 em Intimidação. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Olhos Vermelhos",
    "requirements": {},
    "increase_expertise": ["intimidacao"],
}

pele_corrompida = {
    "formatted_name": "pele_corrompida",
    "description": "Sua carne foi mesclada à matéria vermelha. Você recebe redução de ácido, eletricidade, fogo, frio, luz e trevas 2. Esta RD aumenta em +2 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Pele Corrompida",
    "requirements": {},
}

sangue_acido = {
    "formatted_name": "sangue_acido",
    "description": "Quando você sofre dano por um ataque corpo a corpo, o atacante sofre 1 ponto de dano de ácido por poder da Tormenta que você possui.",
    "requirements": {},
    "name": "Sangue Acido"
}

visco_rubro = {
    "formatted_name": "visco_rubro",
    "description": "Você pode gastar 1 PM para expelir um líquido grosso e corrosivo. Até o final da cena, você recebe +1 nas rolagens de dano corpo a corpo. Este bônus aumenta em +1 para cada dois outros poderes da Tormenta que você possui.",
    "name": "Visco Rubro",
    "requirements": {}
}


TORMENT_POWERS = [(anatomia_insana['name'], anatomia_insana),
                  (antenas['name'], antenas),
                  (armamento_aberrante['name'], armamento_aberrante),
                  (articulacoes_flexiveis['name'], articulacoes_flexiveis),
                  (asas_insetoides['name'], asas_insetoides),
                  (carapaca['name'], carapaca),
                  (corpo_aberrante['name'], corpo_aberrante),
                  (cuspir_enxame['name'], cuspir_enxame),
                  (dentes_afiados['name'], dentes_afiados),
                  (desprezar_realidade['name'], desprezar_realidade),
                  (empunhadura_rubra['name'], empunhadura_rubra),
                  (fome_mana['name'], fome_mana),
                  (larva_explosiva['name'], larva_explosiva),
                  (legiao_aberrante['name'], legiao_aberrante),
                  (maos_membranosas['name'], maos_membranosas),
                  (membros_estendidos['name'], membros_estendidos),
                  (membros_extras['name'], membros_extras),
                  (mente_aberrante['name'], mente_aberrante),
                  (olhos_vermelhos['name'], olhos_vermelhos),
                  (pele_corrompida['name'], pele_corrompida),
                  (sangue_acido['name'], sangue_acido),
                  (visco_rubro['name'], visco_rubro),
                  ]


class PoderTormenta():

    def validate_select_powers(amount_powers: int, current):
        if len(current) != amount_powers:
            remaining_powers = amount_powers - len(current)
            reason_message = f"+{remaining_powers}" if remaining_powers > 0 else remaining_powers
            raise errors.ValidationError(
                "",
                reason=f"Você PRECISA selecionar {reason_message} poderes")  # noqa: E501
        return True

    def select_powers(amount_powers: int, choices):
        message = f"Escolha {amount_powers} poderes"
        questions = [
            inquirer.Checkbox("poder", message=message,
                              choices=choices,
                              carousel=True,
                              validate=lambda _, current: PoderTormenta.validate_select_powers(
                                  amount_powers, current)
                              ),
        ]

        answer = inquirer.prompt(questions)
        poderes = answer['poder']
        return poderes
