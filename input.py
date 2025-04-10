import os

# Make sure the Input folder exists
os.makedirs("Input", exist_ok=True)

# Sample stories in different languages
story_files = {
    "Input/story_en.txt": [
        "Once upon a time in a peaceful village, there lived a kind girl.",
        "She loved reading stories and helping animals.",
        "One day, it started raining heavily.",
        "But she smiled and danced in the rain."
    ],
    "Input/story_hi.txt": [
        "एक बार की बात है, एक शांत गाँव में एक दयालु लड़की रहती थी।",
        "उसे कहानियाँ पढ़ना और जानवरों की मदद करना बहुत पसंद था।",
        "एक दिन बहुत तेज़ बारिश होने लगी।",
        "लेकिन वह मुस्कुराई और बारिश में नाचने लगी।"
    ],
    "Input/story_ml.txt": [
        "ഒരു കാലത്ത് ഒരു സമാധാനപരമായ ഗ്രാമത്തില്‍ ഒരു ദയയുള്ള പെണ്‍കുട്ടി ജീവിച്ചിരുന്നു.",
        "അവള്‍ കഥകള്‍ വായിക്കാന്‍ ഇഷ്ടപ്പെട്ടിരുന്നു, മൃഗങ്ങളെ സഹായിക്കുകയും ചെയ്തു.",
        "ഒരു ദിവസം കനത്ത മഴ പെയ്യുകയും ചെയ്തു.",
        "പക്ഷേ അവള്‍ ചിരിക്കയും മഴയില്‍ നൃത്തം ചെയ്യുകയും ചെയ്തു."
    ],
    "Input/story_fr.txt": [
        "Il était une fois une fille gentille qui vivait dans un village paisible.",
        "Elle aimait lire des histoires et aider les animaux.",
        "Un jour, il a commencé à pleuvoir très fort.",
        "Mais elle a souri et a dansé sous la pluie."
    ],
    "Input/story_es.txt": [
        "Había una vez una niña amable que vivía en un pueblo tranquilo.",
        "Le encantaba leer cuentos y ayudar a los animales.",
        "Un día comenzó a llover muy fuerte.",
        "Pero ella sonrió y bailó bajo la lluvia."
    ],
    "Input/story_de.txt": [
        "Es war einmal ein nettes Mädchen, das in einem friedlichen Dorf lebte.",
        "Sie liebte es, Geschichten zu lesen und Tieren zu helfen.",
        "Eines Tages begann es stark zu regnen.",
        "Aber sie lächelte und tanzte im Regen."
    ],
    "Input/story_ta.txt": [
        "ஒரு காலத்தில் அமைதியான கிராமத்தில் ஒரு நல்ல சிறுமி வாழ்ந்தாள்.",
        "அவளுக்கு கதைகள் படிப்பதும், விலங்குகளுக்கு உதவுவதும் பிடித்தது.",
        "ஒருநாள் மிகுந்த மழை பெய்ய ஆரம்பித்தது.",
        "ஆனால் அவள் சிரித்தாள் மற்றும் மழையில் நடனமாடினாள்."
    ],
    "Input/story_te.txt": [
        "ఒకప్పుడు శాంతమైన గ్రామంలో ఓ మంచి అమ్మాయి ఉండేది.",
        "ఆమెకి కథలు చదవడం, జంతువులకు సహాయం చేయడం చాలా ఇష్టం.",
        "ఒకరోజు భారీగా వర్షం మొదలైంది.",
        "కానీ ఆమె నవ్వింది మరియు వర్షంలో నాట్యం చేసింది."
    ],
    "Input/story_it.txt": [
        "C'era una volta una ragazza gentile che viveva in un villaggio tranquillo.",
        "Le piaceva leggere storie e aiutare gli animali.",
        "Un giorno iniziò a piovere molto forte.",
        "Ma lei sorrise e ballò sotto la pioggia."
    ]
}

# Write each story to a file
for filepath, lines in story_files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
