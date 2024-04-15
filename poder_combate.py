import inquirer
from inquirer import errors
from enum_atributos import AtributosPadrao


acuidade_arma = {
    "formatted_name": "acuidade_arma",
    "name": "Acuidade com Arma",
    "description": "Quando usa uma arma corpo a corpo leve ou uma arma de arremesso, você pode usar sua Destreza em vez de Força nos testes de ataque e rolagens de dano.",
    "requirements": {
        "attributes": [
            {AtributosPadrao.DES: 1}]
    }
}

arma_secundaria_grande = {
    "formatted_name": "arma_secundaria_grande",
    "name": "Arma Secundária Grande",
    "description": "Você pode empunhar duas armas de uma mão com o poder Estilo de Duas Armas.",
    "requirements": {
        "power": {
            "combate": {"items": ["estilo_duas_armas"]}
        }
    }
}

arremesso_potente = {
    "formatted_name": "arremesso_potente",
    "name": "Arremesso Potente",
    "description": "Quando usa uma arma de arremesso, você pode usar sua Força em vez de Destreza nos testes de ataque. Se você possuir o poder Ataque Poderoso, poderá usá-lo com armas de arremesso.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.FOR: 1
        }],
        "power": {
            "combate": {"items": ["estilo_arremesso"]}
        }
    }
}

ataque_pesado = {
    "formatted_name": "ataque_pesado",
    "name": "Ataque Pesado",
    "description": "Quando faz um ataque corpo a corpo com uma arma de duas mãos, você pode pagar 1 PM. Se fizer isso e acertar o ataque, além do dano você faz uma manobra derrubar ou empurrar contra o alvo como uma ação livre (use o resultado do ataque como o teste de manobra).",
    "requirements": {
        "power": {
            "combate": {"items": ["estilo_duas_maos"]}
        }
    }
}

ataque_poderoso = {
    "formatted_name": "ataque_poderoso",
    "name": "Ataque Poderoso",
    "description": "Quando faz um ataque corpo a corpo com uma arma de duas mãos, você pode pagar 1 PM. Se fizer isso e acertar o ataque, além do dano você faz uma manobra derrubar ou empurrar contra o alvo como uma ação livre (use o resultado do ataque como o teste de manobra).",
    "requirements": {
        "attributes": [{
            AtributosPadrao.FOR: 1
        }]
    }
}

ataque_preciso = {
    "formatted_name": "ataque_preciso",
    "name": "Ataque Preciso",
    "description": "Se estiver empunhando uma arma corpo a corpo em uma das mãos e nada na outra, você recebe +2 na margem de ameaça e +1 no multiplicador de crítico.",
    "requirements": {
        "power": {
            "combate": {"items": ["estilo_uma_arma"]}
        }
    }
}

bloqueio_escudo = {
    "formatted_name": "bloqueio_escudo",
    "name": "Bloqueio com Escudo",
    "description": "Quando sofre dano, você pode gastar 1 PM para receber redução de dano igual ao bônus na Defesa que seu escudo fornece contra este dano. Você só pode usar este poder se estiver usando um escudo.",
    "requirements": {
        "power": {
            "combate": {"items": ["estilo_arma_escudo"]}
        }
    }
}

carga_cavalaria = {
    "formatted_name": "carga_cavalaria",
    "name": "Carga de Cavalaria",
    "description": "Quando faz uma investida montada, você causa +2d8 pontos de dano. Além disso, pode continuar se movendo depois do ataque. Você deve se mover em linha reta e seu movimento máximo ainda é o dobro do seu deslocamento.",
    "requirements": {
        "power": {
            "combate": {"items": ["ginete"]}
        }
    }
}


combate_defensivo: {
    "formatted_name": "combate_defensivo",
    "name": "Combate Defensivo",
    "description": "Quando usa a ação agredir, você pode usar este poder. Se fizer isso, até seu próximo turno, sofre -2 em todos os testes de ataque, mas recebe +5 na Defesa.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.INT: 1
        }]
    }
}

derrubar_aprimorado = {
    "formatted_name": "derrubar_aprimorado",
    "name": "Derrubar Aprimorado",
    "description": "Você recebe +2 em testes de ataque para derrubar. Quando derruba uma criatura com essa manobra, pode gastar 1 PM para fazer um ataque extra contra ela.",
    "requirements": {
        "power": {
            "combate": {"items": ["combate_defensivo"]}
        }
    }
}

desarmar_aprimorado = {
    "formatted_name": "desarmar_aprimorado",
    "name": "Desarmar Aprimorado",
    "description": "Você recebe +2 em testes de ataque para desarmar. Quando desarma uma criatura, pode gastar 1 PM para arremessar a arma dela para longe. Para definir onde a arma cai, role  d8 para a direção (sendo “1” diretamente à sua frente, “2” à frente e à direita e assim por diante) e 1d6 para a distância (medida em quadrados de 1,5m a partir da criatura desarmada).",
    "requirements": {
        "power": {
            "combate": {"items": ["combate_defensivo"]}
        }
    }
}

disparo_preciso = {
    "formatted_name": "disparo_preciso",
    "name": "Disparo Preciso",
    "description": "Você pode fazer ataques à distância contra oponentes envolvidos em combate corpo a corpo sem sofrer a penalidade de –5 no teste de ataque.",
    "requirements": {
        "power": {
            "combate": {"items": [["estilo_disparo", "estilo_arremesso"]]}
        }
    }
}

disparo_rapido = {
    "formatted_name": "disparo_rapido",
    "name": "Disparo Preciso",
    "description": "Se estiver empunhando uma arma de disparo que possa recarregar como ação livre e gastar uma ação completa para agredir, pode fazer um ataque adicional com ela. Se fizer isso, sofre -2 em todos os testes de ataque até o seu próximo turno",
    "requirements": {
        "power": {
            "combate": {"items": ["estilo_disparo"]}
        },
        "attributes": [{
            AtributosPadrao.DES: 1
        }]
    }
}

empunhadura_poderosa = {
    "formatted_name": "empunhadura_poderosa",
    "name": "Empunhadura Poderosa",
    "description": "Ao usar uma arma feita para uma categoria de tamanho maior que a sua, a penalidade que você sofre nos testes de ataque diminui para –2 (normalmente, usar uma arma de uma categoria de tamanho maior impõe –5 nos testes de ataque).",
    "requirements": {
        "attributes": [{
            AtributosPadrao.FOR: 3
        }]
    }
}

encouracado = {
    "formatted_name": "encouracado",
    "name": "Encouraçado",
    "description": "Se estiver usando uma armadura pesada, você recebe +2 na Defesa. Esse bônus aumenta em +2 para cada outro poder que você possua que tenha Encouraçado como pré-requisito.",
    "requirements": {
        "others": ["proficiencia_armadura_pesada"]
    }
}

esquiva = {
    "formatted_name": "esquiva",
    "name": "Esquiva",
    "description": "Você recebe +2 na Defesa e Reflexos.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.DES: 1
        }]
    }
}

estilo_arma_escudo = {
    "formatted_name": "estilo_arma_escudo",
    "name": "Estilo de Arma e Escudo",
    "description": "Se você estiver usando um escudo, o bônus na Defesa que ele fornece aumenta em +2.",
    "requirements": {
        "others": ["proficiencia_escudos"],
        "expertises": ["luta"]
    }

}

estilo_arma_longa = {
    "formatted_name": "estilo_arma_longa",
    "name": "Estilo de Arma Longa",
    "description": "Você recebe +2 em testes de ataque com armas alongadas e pode atacar alvos adjacentes com essas armas.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.FOR: 1
        }],
        "expertises": ["luta"]
    }
}

estilo_arremesso = {
    "formatted_name": "estilo_arremesso",
    "name": "Estilo de Arremesso",
    "description": "Você pode sacar armas de arremesso como uma ação livre e recebe +2 nas rolagens de dano com elas. Se também possuir o poder Saque Rápido, também recebe +2 nos testes de ataque com essas armas.",
    "requirements": {
        "expertises": ["pontaria"]
    }
}

estilo_disparo = {
    "formatted_name": "estilo_disparo",
    "name": "Estilo de Disparo",
    "description": "Se estiver usando uma arma de disparo, você soma sua Destreza nas rolagens de dano.",
    "requirements": {
        "expertises": ["pontaria"]
    }
}

estilo_duas_armas = {
    "formatted_name": "estilo_duas_armas",
    "name": "Estilo de Duas Armas",
    "description": "Se estiver empunhando duas armas (e pelo menos uma delas for leve) e fizer a  ação agredir, você pode fazer dois ataques, um com cada arma. Se fizer isso, sofre -2 em todos os testes de ataque até o seu próximo turno. Se possuir Ambidestria, em vez disso não sofre penalidade para usá-lo.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.DES: 2
        }],
        "expertises": ["luta"]
    }
}

estilo_duas_armas = {
    "formatted_name": "estilo_duas_armas",
    "name": "Estilo de Duas Mãos",
    "description": "Se estiver usando uma arma corpo a corpo com as duas mãos, você recebe +5 nas rolagens de dano. Este poder não pode ser usado com armas leves.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.FOR: 2
        }],
        "expertises": ["luta"]
    }
}

estilo_uma_arma = {
    "formatted_name": "estilo_uma_arma",
    "name": "Estilo de Uma Arma",
    "description": "Se estiver usando uma arma corpo a corpo em uma das mãos e nada na outra, você recebe +2 na Defesa e nos testes de ataque com essa arma (exceto ataques desarmados).",
    "requirements": {
        "expertises": ["luta"]
    }
}

estilo_desarmado = {
    "formatted_name": "estilo_desarmado",
    "name": "Estilo Desarmado",
    "description": "Seus ataques desarmados causam 1d6 pontos de dano e podem causar dano letal ou não letal (sem penalidades)",
    "requirements": {
        "expertises": ["luta"]
    }
}

fanatico = {
    "formatted_name": "fanatico",
    "name": "Fanático",
    "description": "Seu deslocamento não é reduzido por usar armaduras pesadas.",
    "requirements": {
        "power": {
            "combate": {"items": ["encouracado"]}
        },
        "level": 12
    }
}

finta_aprimorada = {
    "formatted_name": "Finta Aprimorada",
    "name": "Finta Aprimorada",
    "description": "Você recebe +2 em testes de Enganação para fintar e pode fintar como uma ação de movimento.",
    "requirements": {
        "expertises": ["enganacao"]
    }
}

foco_arma = {
    "formatted_name": "foco_arma",
    "name": "Foco em Arma",
    "description": "Escolha uma arma. Você recebe +2 em testes de ataque com essa arma. Você pode escolher este poder outras vezes para armas diferentes.",
    "requirements": {
        "others": ["proficiencia_com_arma"]
    }
}

ginete = {
    "formatted_name": "ginete",
    "name": "Ginete",
    "description": "Você passa automaticamente em testes de Cavalgar para não cair da montaria quando sofre dano. Além disso, não sofre penalidades para atacar à distância ou lançar  magias quando montado",
    "requirements": {
        "expertises": ["cavalgar"]
    }
}

inexpugnavel = {
    "formatted_name": "inexpugnavel",
    "name": "Inexpugnável",
    "description": "Se estiver usando uma armadura pesada, você recebe +2 em todos os testes de resistência.",
    "requirements": {
        "power": {
            "combate": {"items": ["encouracado"]}
        },
        "level": 6
    }
}

mira_apurada = {
    "formatted_name": "mira_apurada",
    "name": "Mira Apurada",
    "description": "Quando usa a ação mirar, você recebe +2 em testes de ataque e na margem de ameaça com ataques à distância até o fim do turno.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.SAB: 1
        }],
        "power": {
            "combate": {"items": ["disparo_preciso"]}
        }
    }
}

piqueiro = {
    "formatted_name": "piqueiro",
    "name": "Piqueiro",
    "description": "Uma vez por rodada, se estiver empunhando uma arma alongada e um inimigo entrar voluntariamente em seu alcance corpo a orpo, você pode gastar 1 PM para fazer um ataque corpo a corpo contra este oponente com esta arma. Se o oponente tiver se aproximado fazendo uma investida, seu ataque causa dois dados de dano extra do mesmo tipo",
    "requirements": {
        "power": {
            "combate": {"items": ["estilo_arma_longa"]}
        }
    }
}

presenca_aterradora = {
    "formatted_name": "presenca_aterradora",
    "name": "Presença Aterradora",
    "description": "Você pode gastar uma ação padrão e 1 PM para assustar todas as criaturas a sua escolha em alcance curto. Veja a perícia Intimidação para as regras de assustar.",
    "requirements": {
        "expertises": [{"intimidacao": 1}]
    }
}

proficiencia = {
    "formatted_name": "proficiencia",
    "name": "Proficiência",
    "description": "Escolha uma proficiência: armas marciais, armas de fogo, armaduras pesadas ou escudos (se for proficiente em armas marciais, você também pode escolher armas exóticas). Você recebe essa proficiência. Você pode escolher este poder outras vezes para proficiências diferentes.",
    "requirements": {}
}

quebrar_aprimorado = {
    "formatted_name": "quebrar_aprimorado",
    "name": "Quebrar Aprimorado",
    "description": "Você recebe +2 em testes de ataque para quebrar. Quando reduz os PV de uma arma para 0 ou menos, você pode gastar 1 PM para realizar um ataque extra contra o usuário ela. O ataque adicional usa os mesmos valores de ataque e dano, mas os dados devem ser rolados novamente.",
    "requirements": {
        "power": {
            "combate": {
                "items": ["ataque_poderoso"]
            }
        }
    }
}

reflexos_combate = {
    "formatted_name": "reflexos_combate",
    "name": "Reflexos de Combate",
    "description": "Você ganha uma ação de movimento extra no seu primeiro turno de cada combate.",
    "requirements": {
        "attributes": [{
            AtributosPadrao.DES: 1
        }]
    }
}

saque_rapido = {
    "formatted_name": "saque_rapido",
    "name": "Saque Rápido",
    "description": "Você recebe +2 em Iniciativa e pode sacar ou guardar itens como uma ação livre (em vez de ação de movimento). Além disso, a ação que você gasta para recarregar armas de disparo diminui em uma categoria (ação completa para padrão, padrão para movimento, movimento para livre).",
    "requirements": {
        "expertises": [{"iniciativa": 1}]
    }
}

trespassar = {
    "formatted_name": "trespassar",
    "name": "Trespassar",
    "description": "Quando você faz um ataque corpo a corpo e reduz os pontos de vida do alvo para 0 ou menos, pode gastar 1 PM para fazer um ataque adicional contra outra criatura dentro do seu alcance.",
    "requirements": {
        "power": {
            "combate": {
                "items"["ataque_poderoso"]
            }
        }
    }
}

vitalidade = {
    "formatted_name": "vitalidade",
    "name": "Vitalidade",
    "description": "Você recebe +1 PV por nível de personagem e +2 em Fortitude.",
    "requirements": {
        "attributes": {
            AtributosPadrao.CON: 1
        }
    }
}

COMBAT_POWERS = [(acuidade_arma["name"], acuidade_arma["formatted_name"]),
                 (arma_secundaria_grande["name"],
                  arma_secundaria_grande["formatted_name"]),
                 (arremesso_potente["name"],
                  arremesso_potente["formatted_name"]),
                 (ataque_pesado["name"], ataque_pesado["formatted_name"]),
                 (ataque_poderoso["name"], ataque_poderoso["formatted_name"]),
                 (ataque_preciso["name"], ataque_preciso["formatted_name"]),
                 (bloqueio_escudo["name"], bloqueio_escudo["formatted_name"]),
                 (carga_cavalaria["name"], carga_cavalaria["formatted_name"]),
                 (derrubar_aprimorado["name"],
                  derrubar_aprimorado["formatted_name"]),
                 (desarmar_aprimorado["name"],
                  desarmar_aprimorado["formatted_name"]),
                 (disparo_preciso["name"], disparo_preciso["formatted_name"]),
                 (disparo_rapido["name"], disparo_rapido["formatted_name"]),
                 (empunhadura_poderosa["name"],
                  empunhadura_poderosa["formatted_name"]),
                 (encouracado["name"], encouracado["formatted_name"]),
                 (esquiva["name"], esquiva["formatted_name"]),
                 (estilo_arma_escudo["name"],
                  estilo_arma_escudo["formatted_name"]),
                 (estilo_arma_longa["name"],
                  estilo_arma_longa["formatted_name"]),
                 (estilo_arremesso["name"],
                  estilo_arremesso["formatted_name"]),
                 (estilo_disparo["name"], estilo_disparo["formatted_name"]),
                 (estilo_duas_armas["name"],
                  estilo_duas_armas["formatted_name"]),
                 (estilo_duas_armas["name"],
                  estilo_duas_armas["formatted_name"]),
                 (estilo_uma_arma["name"], estilo_uma_arma["formatted_name"]),
                 (estilo_desarmado["name"],
                  estilo_desarmado["formatted_name"]),
                 (fanatico["name"], fanatico["formatted_name"]),
                 (finta_aprimorada["name"],
                  finta_aprimorada["formatted_name"]),
                 (foco_arma["name"], foco_arma["formatted_name"]),
                 (ginete["name"], ginete["formatted_name"]),
                 (inexpugnavel["name"], inexpugnavel["formatted_name"]),
                 (mira_apurada["name"], mira_apurada["formatted_name"]),
                 (piqueiro["name"], piqueiro["formatted_name"]),
                 (presenca_aterradora["name"],
                  presenca_aterradora["formatted_name"]),
                 (proficiencia["name"], proficiencia["formatted_name"]),
                 (quebrar_aprimorado["name"],
                  quebrar_aprimorado["formatted_name"]),
                 (reflexos_combate["name"],
                  reflexos_combate["formatted_name"]),
                 (saque_rapido["name"], saque_rapido["formatted_name"]),
                 (trespassar["name"], trespassar["formatted_name"]),
                 (vitalidade["name"], vitalidade["formatted_name"])]


class PoderCombate():
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
                              validate=lambda _, current: PoderCombate.validate_select_powers(
                                  amount_powers, current)
                              ),
        ]
        answer = inquirer.prompt(questions)
        poderes = answer['poder']
        return poderes
