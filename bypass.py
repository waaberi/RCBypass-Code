import random
from tkinter import Tk

lmao = [
    {
        "base": "A",
        "letters": "ⒶＡÀÁÂẦẤẪẨÃĀĂẰẮẴẲȦǠÄǞẢÅǺǍȀȂẠẬẶḀĄȺⱯ",
    },
    {
        "base": "B",
        "letters": "ⒷＢḂḄḆɃƂƁ",
    },
    {
        "base": "C",
        "letters": "ⒸＣĆĈĊČÇḈƇȻꜾ",
    },
    {
        "base": "D",
        "letters": "ⒹＤḊĎḌḐḒḎĐƋƊƉꝹ",
    },
    {
        "base": "E",
        "letters": "ⒺＥÈÉÊỀẾỄỂẼĒḔḖĔĖËẺĚȄȆẸỆȨḜĘḘḚƐƎ",
    },
    {
        "base": "F",
        "letters": "ⒻＦḞƑꝻ",
    },
    {
        "base": "G",
        "letters": "ⒼＧǴĜḠĞĠǦĢǤƓꞠꝽꝾ",
    },
    {
        "base": "H",
        "letters": "ⒽＨĤḢḦȞḤḨḪĦⱧⱵꞍ",
    },
    {
        "base": "I",
        "letters": "ⒾＩÌÍÎĨĪĬİÏḮỈǏȈȊỊĮḬƗ",
    },
    {
        "base": "J",
        "letters": "ⒿＪĴɈ",
    },
    {
        "base": "K",
        "letters": "ⓀＫḰǨḲĶḴƘⱩꝀꝂꝄꞢ",
    },
    {
        "base": "L",
        "letters": "ⓁＬĿĹĽḶḸĻḼḺŁȽⱢⱠꝈꝆꞀ",
    },
    {
        "base": "M",
        "letters": "ⓂＭḾṀṂⱮƜ",
    },
    {
        "base": "N",
        "letters": "ⓃＮǸŃÑṄŇṆŅṊṈȠƝꞐꞤ",
    },
    {
        "base": "O",
        "letters": "ⓄＯÒÓÔỒỐỖỔÕṌȬṎŌṐṒŎȮȰÖȪỎŐǑȌȎƠỜỚỠỞỢỌỘǪǬØǾƆƟꝊꝌ",
    },
    {
        "base": "P",
        "letters": "ⓅＰṔṖƤⱣꝐꝒꝔ",
    },
    {
        "base": "Q",
        "letters": "ⓆＱꝖꝘɊ",
    },
    {
        "base": "R",
        "letters": "ⓇＲŔṘŘȐȒṚṜŖṞɌⱤꝚꞦꞂ",
    },
    {
        "base": "S",
        "letters": "ⓈＳẞŚṤŜṠŠṦṢṨȘŞⱾꞨꞄ",
    },
    {
        "base": "T",
        "letters": "ⓉＴṪŤṬȚŢṰṮŦƬƮȾꞆ",
    },
    {
        "base": "U",
        "letters": "ⓊＵÙÚÛŨṸŪṺŬÜǛǗǕǙỦŮŰǓȔȖƯỪỨỮỬỰỤṲŲṶṴɄ",
    },
    {
        "base": "V",
        "letters": "ⓋＶṼṾƲꝞɅ",
    },
    {
        "base": "W",
        "letters": "ⓌＷẀẂŴẆẄẈⱲ",
    },
    {
        "base": "X",
        "letters": "ⓍＸẊẌ",
    },
    {
        "base": "Y",
        "letters": "ⓎＹỲÝŶỸȲẎŸỶỴƳɎỾ",
    },
    {
        "base": "Z",
        "letters": "ⓏＺŹẐŻŽẒẔƵȤⱿⱫꝢ",
    },
    {
        "base": "a",
        "letters": "ⓐａẚàáâầấẫẩãāăằắẵẳȧǡäǟảåǻǎȁȃạậặḁąⱥɐ",
    },
    {
        "base": "b",
        "letters": "ⓑｂḃḅḇƀƃɓ",
    },
    {
        "base": "c",
        "letters": "ⓒｃćĉċčçḉƈȼꜿↄ",
    },
    {
        "base": "d",
        "letters": "ⓓｄḋďḍḑḓḏđƌɖɗꝺ",
    },
    {
        "base": "e",
        "letters": "ⓔｅèéêềếễểẽēḕḗĕėëẻěȅȇẹệȩḝęḙḛɇɛǝ",
    },
    {
        "base": "f",
        "letters": "ⓕｆḟƒꝼ",
    },
    {
        "base": "g",
        "letters": "ⓖｇǵĝḡğġǧģǥɠꞡᵹꝿ",
    },
    {
        "base": "h",
        "letters": "ⓗｈĥḣḧȟḥḩḫẖħⱨⱶɥ",
    },
    {
        "base": "i",
        "letters": "ⓘｉìíîĩīĭïḯỉǐȉȋịįḭɨı",
    },
    {
        "base": "j",
        "letters": "ⓙｊĵǰɉ",
    },
    {
        "base": "k",
        "letters": "ⓚｋḱǩḳķḵƙⱪꝁꝃꝅꞣ",
    },
    {
        "base": "l",
        "letters": "ⓛｌŀĺľḷḹļḽḻſłƚɫⱡꝉꞁꝇ",
    },
    {
        "base": "m",
        "letters": "ⓜｍḿṁṃɱɯ",
    },
    {
        "base": "n",
        "letters": "ⓝｎǹńñṅňṇņṋṉƞɲŉꞑꞥ",
    },
    {
        "base": "o",
        "letters": "ⓞｏòóôồốỗổõṍȭṏōṑṓŏȯȱöȫỏőǒȍȏơờớỡởợọộǫǭøǿɔꝋꝍɵ",
    },
    {
        "base": "p",
        "letters": "ⓟｐṕṗƥᵽꝑꝓꝕ",
    },
    {
        "base": "q",
        "letters": "ⓠｑɋꝗꝙ",
    },
    {
        "base": "r",
        "letters": "ⓡｒŕṙřȑȓṛṝŗṟɍɽꝛꞧꞃ",
    },
    {
        "base": "s",
        "letters": "ⓢｓßśṥŝṡšṧṣṩșşȿꞩꞅẛ",
    },
    {
        "base": "t",
        "letters": "ⓣｔṫẗťṭțţṱṯŧƭʈⱦꞇ",
    },
    {
        "base": "u",
        "letters": "ⓤｕùúûũṹūṻŭüǜǘǖǚủůűǔȕȗưừứữửựụṳųṷṵʉ",
    },
    {
        "base": "v",
        "letters": "ⓥｖṽṿʋꝟʌ",
    },
    {
        "base": "w",
        "letters": "ⓦｗẁẃŵẇẅẘẉⱳ",
    },
    {
        "base": "x",
        "letters": "ⓧｘẋẍ",
    },
    {
        "base": "y",
        "letters": "ⓨｙỳýŷỹȳẏÿỷẙỵƴɏỿ",
    },
    {
        "base": "z",
        "letters": "ⓩｚźẑżžẓẕƶȥɀⱬꝣ",
    },
]


def search(nameKey, myArray):
    for i in range(len(myArray)):
        if (myArray[i]["base"] == nameKey):
            return myArray[i]


def copy_wsl(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()


print(""" *******     ******  ******                                             
/**////**   **////**/*////**   **   ** ******                           
/**   /**  **    // /*   /**  //** ** /**///**  ******    ******  ******
/*******  /**       /******    //***  /**  /** //////**  **////  **//// 
/**///**  /**       /*//// **   /**   /******   ******* //***** //***** 
/**  //** //**    **/*    /**   **    /**///   **////**  /////** /////**
/**   //** //****** /*******   **     /**     //******** ******  ****** 
//     //   //////  ///////   //      //       //////// //////  //////

One of the best filter bypasses available at the moment.
Made by Wabz

""")

while True:
    inp = input("Enter text: ")
    output = ""

    for i in range(len(inp)):
        try:
            resThing = search(inp[i], lmao)["letters"]
            output += random.choice(resThing)
        except:
            output += inp[i]
    copy_wsl(output)
    print(output + " | (copied to clipboard)")
