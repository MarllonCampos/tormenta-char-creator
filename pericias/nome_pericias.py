from pericias import acrobacia as acrobaciaClass
from pericias import adestramento as adestramentoClass
from pericias import atletismo as atletismoClass
from pericias import atuacao as atuacaoClass
from pericias import cavalgar as cavalgarClass
from pericias import conhecimento as conhecimentoClass
from pericias import cura as curaClass
from pericias import diplomacia as diplomaciaClass
from pericias import enganacao as enganacaoClass
from pericias import fortitude as fortitudeClass
from pericias import furtividade as furtividadeClass
from pericias import guerra as guerraClass
from pericias import iniciativa as iniciativaClass
from pericias import intimidacao as intimidacaoClass
from pericias import intuicao as intuicaoClass
from pericias import investigacao as investigacaoClass
from pericias import jogatina as jogatinaClass
from pericias import ladinagem as ladinagemClass
from pericias import luta as lutaClass
from pericias import misticismo as misticismoClass
from pericias import nobreza as nobrezaClass
from pericias import percepcao as percepcaoClass
from pericias import pilotagem as pilotagemClass
from pericias import pontaria as pontariaClass
from pericias import reflexos as reflexosClass
from pericias import religiao as religiaoClass
from pericias import sobrevivencia as sobrevivenciaClass
from pericias import vontade as vontadeClass
from enum import Enum


class NomePericias(Enum):
    acrobacia = "Acrobacia"
    adestramento = "Adestramento"
    atletismo = "Atletismo"
    atuacao = "Atuacao"
    cavalgar = "Cavalgar"
    conhecimento = "Conhecimento"
    cura = "Cura"
    diplomacia = "Diplomacia"
    enganacao = "Enganacao"
    fortitude = "Fortitude"
    furtividade = "Furtividade"
    guerra = "Guerra"
    iniciativa = "Iniciativa"
    intimidacao = "Intimidacao"
    intuicao = "Intuicao"
    investigacao = "Investigacao"
    jogatina = "Jogatina"
    ladinagem = "Ladinagem"
    luta = "Luta"
    misticismo = "Misticismo"
    nobreza = "Nobreza"
    percepcao = "Percepcao"
    pilotagem = "Pilotagem"
    pontaria = "Pontaria"
    reflexos = "Reflexos"
    religiao = "Religiao"
    sobrevivencia = "Sobrevivencia"
    vontade = "Vontade"

    @classmethod
    def expertise_class(cls, name):
        match name:
            case cls.acrobacia.name:
                return acrobaciaClass.Acrobacia()
            case cls.adestramento.name:
                return adestramentoClass.Adestramento()
            case cls.atletismo.name:
                return atletismoClass.Atletismo()
            case cls.atuacao.name:
                return atuacaoClass.Atuacao()
            case cls.cavalgar.name:
                return cavalgarClass.Cavalgar()
            case cls.conhecimento.name:
                return conhecimentoClass.Conhecimento()
            case cls.cura.name:
                return curaClass.Cura()
            case cls.diplomacia.name:
                return diplomaciaClass.Diplomacia()
            case cls.enganacao.name:
                return enganacaoClass.Enganacao()
            case cls.fortitude.name:
                return fortitudeClass.Fortitude()
            case cls.furtividade.name:
                return furtividadeClass.Furtividade()
            case cls.guerra.name:
                return guerraClass.Guerra()
            case cls.iniciativa.name:
                return iniciativaClass.Iniciativa()
            case cls.intimidacao.name:
                return intimidacaoClass.Intimidacao()
            case cls.intuicao.name:
                return intuicaoClass.Intuicao()
            case cls.investigacao.name:
                return investigacaoClass.Investigacao()
            case cls.jogatina.name:
                return jogatinaClass.Jogatina()
            case cls.ladinagem.name:
                return ladinagemClass.Ladinagem()
            case cls.luta.name:
                return lutaClass.Luta()
            case cls.misticismo.name:
                return misticismoClass.Misticismo()
            case cls.nobreza.name:
                return nobrezaClass.Nobreza()
            case cls.percepcao.name:
                return percepcaoClass.Percepcao()
            case cls.pilotagem.name:
                return pilotagemClass.Pilotagem()
            case cls.pontaria.name:
                return pontariaClass.Pontaria()
            case cls.reflexos.name:
                return reflexosClass.Reflexos()
            case cls.religiao.name:
                return religiaoClass.Religiao()
            case cls.sobrevivencia.name:
                return sobrevivenciaClass.Sobrevivencia()
            case cls.vontade.name:
                return vontadeClass.Vontade()
