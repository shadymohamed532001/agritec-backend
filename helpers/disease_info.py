# -*- coding: utf-8 -*-
'''
Bilingual (English / Arabic) information for every class the plant model can
predict, plus the list of real treatment products that are seeded into the
products table.

`DISEASE_INFO` maps the EXACT class name (as returned by
`helpers.class_names.class_names()`) to a short description and a recommended
treatment, in both English and Arabic.

`TREATMENT_PRODUCTS` is the catalogue of medicines/agro-chemicals that gets
inserted into the `products` table by `seed_diseases.py`. Each product's
`tags` is the list of disease class names it treats, so the existing
tag-based lookup (`get_products_by_tag`) returns the right products for a
given prediction.
'''

# Each product has its own generated package image under public/products/.
def _med(slug):
    return f"/uploads/products/med_{slug}.png"


DISEASE_INFO = {
    "Apple Apple scab": {
        "en": "Apple scab is a fungal disease (Venturia inaequalis) that causes olive-green to black velvety spots on leaves and fruit, leading to early leaf drop and cracked, deformed apples.",
        "ar": "جرب التفاح مرض فطري (Venturia inaequalis) يسبب بقعاً مخملية لونها أخضر زيتوني إلى أسود على الأوراق والثمار، مما يؤدي إلى تساقط مبكر للأوراق وتشقق وتشوه الثمار.",
        "treat_en": "Apply a protectant fungicide (Captan, Mancozeb or Myclobutanil) from bud break, rake and destroy fallen leaves, and prune for good air circulation.",
        "treat_ar": "استخدم مبيداً فطرياً وقائياً (كابتان أو مانكوزيب أو ميكلوبيوتانيل) من بداية تفتح البراعم، واجمع الأوراق المتساقطة وأتلفها، وقلّم الأشجار لتحسين التهوية.",
    },
    "Apple Black rot": {
        "en": "Apple black rot is caused by the fungus Botryosphaeria obtusa. It produces 'frog-eye' leaf spots, branch cankers and a firm black rot on the fruit.",
        "ar": "العفن الأسود في التفاح يسببه فطر Botryosphaeria obtusa، ويظهر على شكل بقع 'عين الضفدع' على الأوراق وتقرحات على الأفرع وعفن أسود صلب على الثمار.",
        "treat_en": "Prune out and burn cankered wood and mummified fruit, then spray a Captan or copper-based fungicide; keep trees healthy and avoid wounds.",
        "treat_ar": "قلّم وأحرق الأفرع المصابة بالتقرحات والثمار المتحجرة، ثم رش مبيداً فطرياً يحتوي على كابتان أو النحاس، وحافظ على صحة الأشجار وتجنّب الجروح.",
    },
    "Apple Cedar apple rust": {
        "en": "Cedar apple rust (Gymnosporangium juniperi-virginianae) causes bright orange-yellow spots on leaves and fruit; it needs both apple and juniper/cedar hosts to complete its cycle.",
        "ar": "صدأ التفاح الأرزي (Gymnosporangium) يسبب بقعاً برتقالية صفراء زاهية على الأوراق والثمار، ويحتاج إلى وجود التفاح والعرعر/الأرز معاً لإكمال دورته.",
        "treat_en": "Spray Myclobutanil or Mancozeb during early leaf growth and, where possible, remove nearby juniper/cedar hosts.",
        "treat_ar": "رش ميكلوبيوتانيل أو مانكوزيب أثناء النمو المبكر للأوراق، وأزل أشجار العرعر/الأرز القريبة إن أمكن.",
    },
    "Apple healthy": {
        "en": "The apple leaf appears healthy with no visible signs of disease.",
        "ar": "ورقة التفاح تبدو سليمة وخالية من أي علامات مرضية ظاهرة.",
        "treat_en": "No treatment needed. Keep up good watering, fertilizing and orchard sanitation.",
        "treat_ar": "لا حاجة للعلاج. حافظ على الري والتسميد الجيد ونظافة البستان.",
    },
    "Cherry (including sour) Powdery mildew": {
        "en": "Powdery mildew (Podosphaera clandestina) coats cherry leaves and shoots with a white powdery growth, distorting young leaves and reducing fruit quality.",
        "ar": "البياض الدقيقي (Podosphaera) يغطي أوراق وأفرع الكرز بطبقة بيضاء دقيقة تشوّه الأوراق الحديثة وتقلل جودة الثمار.",
        "treat_en": "Apply sulfur or Myclobutanil fungicide at first sign, prune to open the canopy, and avoid excess nitrogen.",
        "treat_ar": "استخدم الكبريت أو مبيد ميكلوبيوتانيل عند أول ظهور، وقلّم لفتح المجموع الخضري، وتجنّب الإفراط في التسميد النيتروجيني.",
    },
    "Cherry (including sour) healthy": {
        "en": "The cherry leaf appears healthy with no signs of disease.",
        "ar": "ورقة الكرز تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Maintain regular care and orchard hygiene.",
        "treat_ar": "لا حاجة للعلاج. حافظ على العناية المنتظمة ونظافة البستان.",
    },
    "Corn (maize) Cercospora leaf spot Gray leaf spot": {
        "en": "Gray leaf spot (Cercospora zeae-maydis) creates rectangular gray-to-tan lesions running parallel to the leaf veins, which can merge and blight the whole leaf.",
        "ar": "تبقع الأوراق الرمادي (Cercospora) يسبب بقعاً مستطيلة رمادية إلى بنية فاتحة موازية لعروق الورقة، وقد تتحد لتصيب الورقة بالكامل.",
        "treat_en": "Apply a strobilurin or triazole fungicide (Azoxystrobin / Propiconazole), rotate crops and plough under residue, and grow resistant hybrids.",
        "treat_ar": "استخدم مبيداً فطرياً (أزوكسيستروبين / بروبيكونازول)، وطبّق دورة زراعية وادفن بقايا المحصول، وازرع هجناً مقاومة.",
    },
    "Corn (maize) Common rust": {
        "en": "Common rust (Puccinia sorghi) shows small cinnamon-brown raised pustules scattered on both leaf surfaces; severe infection reduces photosynthesis and yield.",
        "ar": "الصدأ الشائع (Puccinia sorghi) يظهر على شكل بثرات بنية قرفية صغيرة بارزة على سطحي الورقة، والإصابة الشديدة تقلل التمثيل الضوئي والإنتاج.",
        "treat_en": "Use resistant hybrids and apply a fungicide (Propiconazole or Mancozeb) if rust appears early and is spreading.",
        "treat_ar": "استخدم هجناً مقاومة، ورش مبيداً فطرياً (بروبيكونازول أو مانكوزيب) إذا ظهر الصدأ مبكراً وبدأ في الانتشار.",
    },
    "Corn (maize) Northern Leaf Blight": {
        "en": "Northern leaf blight (Exserohilum turcicum) produces long, cigar-shaped gray-green lesions that turn tan and can kill large areas of leaf tissue.",
        "ar": "لفحة الأوراق الشمالية (Exserohilum turcicum) تسبب بقعاً طويلة على شكل سيجار لونها رمادي مخضر ثم تتحول إلى بني، وقد تقتل مساحات كبيرة من الورقة.",
        "treat_en": "Grow resistant hybrids, rotate crops, bury residue, and spray Azoxystrobin or Propiconazole when lesions appear before tasselling.",
        "treat_ar": "ازرع هجناً مقاومة وطبّق دورة زراعية وادفن البقايا، ورش أزوكسيستروبين أو بروبيكونازول عند ظهور البقع قبل طرد النورات.",
    },
    "Corn (maize) healthy": {
        "en": "The corn (maize) leaf appears healthy with no signs of disease.",
        "ar": "ورقة الذرة تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Maintain balanced fertilization and crop rotation.",
        "treat_ar": "لا حاجة للعلاج. حافظ على التسميد المتوازن والدورة الزراعية.",
    },
    "Grape Black rot": {
        "en": "Grape black rot (Guignardia bidwellii) causes tan leaf spots with dark borders and rots berries into hard, black, shrivelled mummies.",
        "ar": "العفن الأسود في العنب (Guignardia bidwellii) يسبب بقعاً بنية على الأوراق بحواف داكنة، ويحوّل الحبات إلى عفن أسود صلب متجعد.",
        "treat_en": "Remove mummified berries and infected canes, then spray Mancozeb or Myclobutanil from early shoot growth through fruit set.",
        "treat_ar": "أزل الحبات المتحجرة والأفرع المصابة، ثم رش مانكوزيب أو ميكلوبيوتانيل من بداية نمو الأفرع حتى عقد الثمار.",
    },
    "Grape Esca (Black Measles)": {
        "en": "Esca (Black Measles) is a complex trunk disease that causes 'tiger-stripe' leaf patterns, dark spots on berries and sudden vine collapse; there is no chemical cure.",
        "ar": "مرض الإسكا (الحصبة السوداء) مرض معقد يصيب جذع الكرمة ويسبب نمطاً مخططاً كـ'جلد النمر' على الأوراق وبقعاً داكنة على الحبات وانهياراً مفاجئاً للكرمة، ولا يوجد علاج كيميائي شافٍ.",
        "treat_en": "There is no cure; prune out and destroy affected wood, protect pruning wounds, and keep vines vigorous. Protectant sprays (Bordeaux mixture) only limit secondary spread.",
        "treat_ar": "لا يوجد علاج شافٍ؛ قلّم وأتلف الأخشاب المصابة، واحمِ جروح التقليم، وحافظ على قوة الكرمات. الرشات الوقائية (محلول بوردو) تحد فقط من الانتشار الثانوي.",
    },
    "Grape Leaf blight (Isariopsis Leaf Spot)": {
        "en": "Isariopsis leaf blight (Pseudocercospora vitis) causes irregular dark-brown leaf spots that merge and cause premature defoliation, weakening the vine.",
        "ar": "لفحة أوراق العنب (Isariopsis) تسبب بقعاً بنية داكنة غير منتظمة تتحد وتؤدي إلى تساقط مبكر للأوراق وإضعاف الكرمة.",
        "treat_en": "Spray a copper-based fungicide or Mancozeb, improve canopy ventilation, and remove fallen infected leaves.",
        "treat_ar": "رش مبيداً نحاسياً أو مانكوزيب، وحسّن تهوية المجموع الخضري، وأزل الأوراق المصابة المتساقطة.",
    },
    "Grape healthy": {
        "en": "The grape leaf appears healthy with no signs of disease.",
        "ar": "ورقة العنب تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Maintain canopy management and routine care.",
        "treat_ar": "لا حاجة للعلاج. حافظ على إدارة المجموع الخضري والعناية الروتينية.",
    },
    "Orange Haunglongbing (Citrus greening)": {
        "en": "Huanglongbing (citrus greening) is a bacterial disease spread by the Asian citrus psyllid. It causes blotchy yellow leaves, lopsided bitter fruit and tree decline; it is fatal and incurable.",
        "ar": "مرض التخضير (Huanglongbing) مرض بكتيري ينقله بسيلا الحمضيات الآسيوية، ويسبب اصفراراً غير منتظم للأوراق وثماراً مشوهة مُرّة وتدهور الشجرة، وهو قاتل ولا علاج له.",
        "treat_en": "There is no cure. Control the psyllid vector with insecticides (Imidacloprid), remove and destroy infected trees, and plant certified disease-free stock.",
        "treat_ar": "لا يوجد علاج. كافح حشرة البسيلا الناقلة بالمبيدات (إيميداكلوبريد)، وأزل الأشجار المصابة وأتلفها، وازرع شتلات معتمدة خالية من المرض.",
    },
    "Peach Bacterial spot": {
        "en": "Bacterial spot (Xanthomonas arboricola) causes small dark angular leaf spots that drop out giving a 'shot-hole' look, plus cracked, pitted fruit.",
        "ar": "التبقع البكتيري (Xanthomonas) يسبب بقعاً صغيرة داكنة زاوية على الأوراق تتساقط فتعطي مظهر 'ثقب الطلقة'، إضافة إلى تشقق وتنقّر الثمار.",
        "treat_en": "Apply copper-based bactericides (early season) and oxytetracycline sprays, grow resistant varieties, and avoid overhead irrigation.",
        "treat_ar": "استخدم مبيدات بكتيرية نحاسية (في بداية الموسم) ورشات أوكسي تتراسيكلين، وازرع أصنافاً مقاومة، وتجنّب الري الرشّي العلوي.",
    },
    "Peach healthy": {
        "en": "The peach leaf appears healthy with no signs of disease.",
        "ar": "ورقة الخوخ تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Continue routine orchard care.",
        "treat_ar": "لا حاجة للعلاج. واصل العناية الروتينية بالبستان.",
    },
    "Pepper bell Bacterial spot": {
        "en": "Bacterial spot (Xanthomonas) on bell pepper causes small water-soaked leaf spots that turn brown with yellow halos, plus scabby raised spots on fruit.",
        "ar": "التبقع البكتيري (Xanthomonas) في الفلفل يسبب بقعاً صغيرة مشبعة بالماء على الأوراق تتحول إلى بني مع هالة صفراء، وبقعاً بارزة خشنة على الثمار.",
        "treat_en": "Use certified clean seed, spray copper-based bactericides, rotate crops, and avoid working plants when wet.",
        "treat_ar": "استخدم بذوراً معتمدة نظيفة، ورش مبيدات بكتيرية نحاسية، وطبّق دورة زراعية، وتجنّب التعامل مع النباتات وهي مبللة.",
    },
    "Pepper bell healthy": {
        "en": "The bell pepper leaf appears healthy with no signs of disease.",
        "ar": "ورقة الفلفل تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Maintain balanced watering and feeding.",
        "treat_ar": "لا حاجة للعلاج. حافظ على ري وتسميد متوازن.",
    },
    "Potato Early blight": {
        "en": "Early blight (Alternaria solani) causes dark brown leaf spots with concentric 'target' rings on older leaves, leading to leaf yellowing and drop.",
        "ar": "اللفحة المبكرة (Alternaria solani) تسبب بقعاً بنية داكنة بحلقات متحدة المركز كـ'الهدف' على الأوراق الأكبر سناً، مما يؤدي إلى اصفرار الأوراق وتساقطها.",
        "treat_en": "Spray Chlorothalonil or Mancozeb, remove infected debris, rotate crops, and avoid overhead watering.",
        "treat_ar": "رش كلوروثالونيل أو مانكوزيب، وأزل البقايا المصابة، وطبّق دورة زراعية، وتجنّب الري العلوي.",
    },
    "Potato Late blight": {
        "en": "Late blight (Phytophthora infestans) causes large dark water-soaked leaf lesions with pale margins and white mould underneath, and can destroy a crop within days in cool, wet weather.",
        "ar": "اللفحة المتأخرة (Phytophthora infestans) تسبب بقعاً كبيرة داكنة مشبعة بالماء بحواف باهتة وعفناً أبيض على السطح السفلي، ويمكن أن تدمر المحصول خلال أيام في الجو البارد الرطب.",
        "treat_en": "Apply Chlorothalonil, Mancozeb or copper fungicide preventively, destroy infected plants, and plant resistant varieties on well-drained soil.",
        "treat_ar": "رش كلوروثالونيل أو مانكوزيب أو مبيداً نحاسياً وقائياً، وأتلف النباتات المصابة، وازرع أصنافاً مقاومة في تربة جيدة الصرف.",
    },
    "Potato healthy": {
        "en": "The potato leaf appears healthy with no signs of disease.",
        "ar": "ورقة البطاطس تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Keep monitoring and maintain crop rotation.",
        "treat_ar": "لا حاجة للعلاج. واصل المراقبة وحافظ على الدورة الزراعية.",
    },
    "Squash Powdery mildew": {
        "en": "Powdery mildew on squash coats leaves and stems with white powdery patches, reducing photosynthesis and causing leaves to yellow and die early.",
        "ar": "البياض الدقيقي في القرع يغطي الأوراق والسيقان بطبقة بيضاء دقيقة تقلل التمثيل الضوئي وتسبب اصفرار الأوراق وموتها مبكراً.",
        "treat_en": "Apply sulfur, potassium bicarbonate or Myclobutanil at first sign, space plants for airflow, and grow resistant varieties.",
        "treat_ar": "استخدم الكبريت أو بيكربونات البوتاسيوم أو ميكلوبيوتانيل عند أول ظهور، وباعد بين النباتات لتحسين التهوية، وازرع أصنافاً مقاومة.",
    },
    "Strawberry Leaf scorch": {
        "en": "Leaf scorch (Diplocarpon earlianum) causes many small dark-purple spots that merge so the leaf looks scorched and dries from the edges.",
        "ar": "لفحة أوراق الفراولة (Diplocarpon earlianum) تسبب بقعاً صغيرة كثيرة بنفسجية داكنة تتحد فتبدو الورقة محترقة وتجف من الحواف.",
        "treat_en": "Remove old infected leaves after harvest, improve air circulation, and apply Captan or a copper-based fungicide.",
        "treat_ar": "أزل الأوراق المصابة القديمة بعد الحصاد، وحسّن التهوية، ورش كابتان أو مبيداً نحاسياً.",
    },
    "Strawberry healthy": {
        "en": "The strawberry leaf appears healthy with no signs of disease.",
        "ar": "ورقة الفراولة تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Maintain good spacing and watering.",
        "treat_ar": "لا حاجة للعلاج. حافظ على التباعد الجيد والري المنتظم.",
    },
    "Tomato Bacterial spot": {
        "en": "Bacterial spot (Xanthomonas) on tomato causes small dark greasy leaf spots with yellow halos and scabby spots on fruit, worsened by warm wet weather.",
        "ar": "التبقع البكتيري (Xanthomonas) في الطماطم يسبب بقعاً صغيرة داكنة دهنية على الأوراق مع هالة صفراء وبقعاً خشنة على الثمار، ويزداد سوءاً في الجو الدافئ الرطب.",
        "treat_en": "Use clean certified seed, spray copper-based bactericides, rotate crops, and avoid overhead irrigation and handling wet plants.",
        "treat_ar": "استخدم بذوراً معتمدة نظيفة، ورش مبيدات بكتيرية نحاسية، وطبّق دورة زراعية، وتجنّب الري العلوي ولمس النباتات وهي مبللة.",
    },
    "Tomato Early blight": {
        "en": "Early blight (Alternaria solani) causes dark concentric 'target' spots on lower tomato leaves, with yellowing and defoliation that exposes fruit to sunscald.",
        "ar": "اللفحة المبكرة (Alternaria solani) تسبب بقعاً داكنة بحلقات متحدة المركز كـ'الهدف' على أوراق الطماطم السفلية، مع اصفرار وتساقط يعرّض الثمار لحروق الشمس.",
        "treat_en": "Spray Chlorothalonil or Mancozeb, mulch to limit soil splash, stake plants, and remove infected lower leaves.",
        "treat_ar": "رش كلوروثالونيل أو مانكوزيب، وضع غطاء (مالش) لتقليل تطاير التربة، وادعم النباتات، وأزل الأوراق السفلية المصابة.",
    },
    "Tomato Late blight": {
        "en": "Late blight (Phytophthora infestans) causes large greasy gray-green leaf blotches with white mould and rapidly rotting fruit; it spreads explosively in cool, humid conditions.",
        "ar": "اللفحة المتأخرة (Phytophthora infestans) تسبب بقعاً كبيرة دهنية رمادية مخضرة مع عفن أبيض وتعفناً سريعاً للثمار، وتنتشر بسرعة كبيرة في الجو البارد الرطب.",
        "treat_en": "Apply Chlorothalonil or Mancozeb preventively, destroy infected plants immediately, avoid overhead watering, and grow resistant varieties.",
        "treat_ar": "رش كلوروثالونيل أو مانكوزيب وقائياً، وأتلف النباتات المصابة فوراً، وتجنّب الري العلوي، وازرع أصنافاً مقاومة.",
    },
    "Tomato Leaf Mold": {
        "en": "Leaf mold (Passalora fulva) causes pale yellow spots on the upper leaf surface and olive-green velvety mould underneath, common in humid greenhouses.",
        "ar": "عفن الأوراق (Passalora fulva) يسبب بقعاً صفراء باهتة على السطح العلوي للورقة وعفناً مخملياً أخضر زيتوني على السطح السفلي، وهو شائع في الصوب الرطبة.",
        "treat_en": "Lower humidity and improve ventilation, avoid wetting leaves, and apply Chlorothalonil or a copper-based fungicide.",
        "treat_ar": "اخفض الرطوبة وحسّن التهوية، وتجنّب ترطيب الأوراق، ورش كلوروثالونيل أو مبيداً نحاسياً.",
    },
    "Tomato Septoria leaf spot": {
        "en": "Septoria leaf spot (Septoria lycopersici) causes many small circular spots with dark borders and gray centres on lower leaves, leading to heavy defoliation.",
        "ar": "تبقع الأوراق السبتوري (Septoria lycopersici) يسبب بقعاً دائرية صغيرة كثيرة بحواف داكنة ومراكز رمادية على الأوراق السفلية، مما يؤدي إلى تساقط شديد للأوراق.",
        "treat_en": "Remove infected leaves, mulch, rotate crops, and spray Chlorothalonil or Mancozeb at first symptoms.",
        "treat_ar": "أزل الأوراق المصابة، وضع غطاء (مالش)، وطبّق دورة زراعية، ورش كلوروثالونيل أو مانكوزيب عند أول الأعراض.",
    },
    "Tomato Spider mites Two-spotted spider mite": {
        "en": "Two-spotted spider mites cause fine yellow stippling and bronzing of leaves with fine webbing; populations explode in hot, dry conditions.",
        "ar": "العنكبوت الأحمر ذو البقعتين يسبب تنقيطاً أصفر دقيقاً وبرونزة على الأوراق مع نسيج عنكبوتي دقيق، وتتكاثر أعداده بشدة في الجو الحار الجاف.",
        "treat_en": "Spray a miticide (Abamectin) or insecticidal soap/horticultural oil, raise humidity, and conserve natural predatory mites.",
        "treat_ar": "رش مبيداً للأكاروسات (أبامكتين) أو صابوناً حشرياً/زيتاً بستانياً، وارفع الرطوبة، وحافظ على الأعداء الطبيعية المفترسة.",
    },
    "Tomato Target Spot": {
        "en": "Target spot (Corynespora cassiicola) causes brown leaf spots with concentric rings and sunken lesions on fruit, leading to defoliation in warm humid weather.",
        "ar": "بقعة الهدف (Corynespora cassiicola) تسبب بقعاً بنية بحلقات متحدة المركز على الأوراق وبقعاً غائرة على الثمار، مما يؤدي إلى تساقط الأوراق في الجو الدافئ الرطب.",
        "treat_en": "Spray Azoxystrobin or Chlorothalonil, improve air circulation, and remove crop debris after harvest.",
        "treat_ar": "رش أزوكسيستروبين أو كلوروثالونيل، وحسّن التهوية، وأزل بقايا المحصول بعد الحصاد.",
    },
    "Tomato Tomato Yellow Leaf Curl Virus": {
        "en": "Tomato yellow leaf curl virus (TYLCV) is spread by whiteflies and causes upward leaf curling, yellowing, stunting and severe flower/fruit drop; there is no cure.",
        "ar": "فيروس تجعد واصفرار أوراق الطماطم (TYLCV) ينقله الذباب الأبيض ويسبب تجعّد الأوراق للأعلى واصفرارها وتقزّم النبات وتساقطاً شديداً للأزهار والثمار، ولا علاج له.",
        "treat_en": "There is no cure. Control whiteflies with insecticides (Imidacloprid) and sticky traps, use reflective mulch and resistant varieties, and remove infected plants.",
        "treat_ar": "لا يوجد علاج. كافح الذباب الأبيض بالمبيدات (إيميداكلوبريد) والمصائد اللاصقة، واستخدم المالش العاكس والأصناف المقاومة، وأزل النباتات المصابة.",
    },
    "Tomato Tomato mosaic virus": {
        "en": "Tomato mosaic virus (ToMV) causes mottled light/dark green leaves, distorted fern-like leaflets and mottled fruit; it spreads by contact and on tools and seed.",
        "ar": "فيروس موزاييك الطماطم (ToMV) يسبب تبرقش الأوراق بلونين أخضر فاتح وداكن وتشوّه الوريقات وتبرقش الثمار، وينتقل باللمس وعلى الأدوات والبذور.",
        "treat_en": "There is no cure. Remove and destroy infected plants, disinfect hands and tools, use resistant varieties and certified seed, and avoid tobacco use near plants.",
        "treat_ar": "لا يوجد علاج. أزل النباتات المصابة وأتلفها، وعقّم اليدين والأدوات، واستخدم أصنافاً مقاومة وبذوراً معتمدة، وتجنّب استخدام التبغ قرب النباتات.",
    },
    "Tomato healthy": {
        "en": "The tomato leaf appears healthy with no signs of disease.",
        "ar": "ورقة الطماطم تبدو سليمة وخالية من علامات المرض.",
        "treat_en": "No treatment needed. Maintain consistent watering, feeding and staking.",
        "treat_ar": "لا حاجة للعلاج. حافظ على ري وتسميد ودعامة منتظمة.",
    },
    "cotton Aphids": {
        "en": "Cotton aphids suck sap from leaves, causing curling, yellowing and sticky honeydew that leads to sooty mould and reduced yield.",
        "ar": "منّ القطن يمتص العصارة من الأوراق مسبباً تجعّدها واصفرارها وإفراز ندوة عسلية لزجة تؤدي إلى العفن الهبابي وانخفاض الإنتاج.",
        "treat_en": "Spray insecticidal soap or a systemic insecticide (Imidacloprid) when thresholds are reached, and conserve natural enemies like ladybirds.",
        "treat_ar": "رش الصابون الحشري أو مبيداً جهازياً (إيميداكلوبريد) عند بلوغ الحد الحرج، وحافظ على الأعداء الطبيعية مثل الدعسوقة (أبو العيد).",
    },
    "cotton Army worm": {
        "en": "Armyworms are caterpillars that chew leaves, buds and bolls, often defoliating cotton rapidly in large numbers.",
        "ar": "الدودة الجيشية يرقات تتغذى على الأوراق والبراعم واللوز، وكثيراً ما تسبب تعرية سريعة للقطن بأعدادها الكبيرة.",
        "treat_en": "Scout regularly and spray a selective insecticide (Spinosad or Bacillus thuringiensis) while larvae are small; hand-pick in small plots.",
        "treat_ar": "افحص الحقل بانتظام ورش مبيداً انتقائياً (سبينوساد أو بكتيريا Bt) واليرقات صغيرة، والتقطها يدوياً في المساحات الصغيرة.",
    },
    "cotton Bacterial Blight": {
        "en": "Bacterial blight (Xanthomonas citri pv. malvacearum) causes angular water-soaked leaf spots, black vein streaks and boll rot in cotton.",
        "ar": "اللفحة البكتيرية (Xanthomonas) تسبب بقعاً زاوية مشبعة بالماء على الأوراق وتخطيطاً أسود على العروق وتعفّن اللوز في القطن.",
        "treat_en": "Plant resistant varieties and acid-delinted certified seed, apply copper-based sprays, and remove and destroy infected residue.",
        "treat_ar": "ازرع أصنافاً مقاومة وبذوراً معتمدة منزوعة الزغب، ورش مبيدات نحاسية، وأزل البقايا المصابة وأتلفها.",
    },
    "cotton Healthy": {
        "en": "The cotton leaf appears healthy with no signs of disease or pests.",
        "ar": "ورقة القطن تبدو سليمة وخالية من علامات المرض أو الآفات.",
        "treat_en": "No treatment needed. Continue scouting and balanced crop management.",
        "treat_ar": "لا حاجة للعلاج. واصل فحص الحقل والإدارة المتوازنة للمحصول.",
    },
    "cotton Powdery Mildew": {
        "en": "Powdery mildew coats cotton leaves with white powdery growth that reduces photosynthesis and can cause premature leaf drop.",
        "ar": "البياض الدقيقي يغطي أوراق القطن بطبقة بيضاء دقيقة تقلل التمثيل الضوئي وقد تسبب تساقطاً مبكراً للأوراق.",
        "treat_en": "Apply sulfur or a suitable fungicide at first sign, avoid excess nitrogen, and improve air circulation.",
        "treat_ar": "استخدم الكبريت أو مبيداً فطرياً مناسباً عند أول ظهور، وتجنّب الإفراط في النيتروجين، وحسّن التهوية.",
    },
    "cotton Target spot": {
        "en": "Target spot (Corynespora cassiicola) on cotton causes brown lesions with concentric rings, leading to defoliation under warm humid conditions.",
        "ar": "بقعة الهدف (Corynespora cassiicola) في القطن تسبب بقعاً بنية بحلقات متحدة المركز تؤدي إلى تساقط الأوراق في الظروف الدافئة الرطبة.",
        "treat_en": "Spray Azoxystrobin or Chlorothalonil, improve airflow, and remove crop residue after harvest.",
        "treat_ar": "رش أزوكسيستروبين أو كلوروثالونيل، وحسّن التهوية، وأزل بقايا المحصول بعد الحصاد.",
    },
}


def get_disease_information(class_name):
    '''Return a bilingual (EN + AR) description + recommended treatment string
    for a predicted class, or None if the class is unknown.'''
    info = DISEASE_INFO.get(class_name)
    if not info:
        return None
    return (
        f"{info['en']}\n\n"
        f"Recommended treatment: {info['treat_en']}\n\n"
        f"----------\n\n"
        f"{info['ar']}\n\n"
        f"العلاج الموصى به: {info['treat_ar']}"
    )


# ---------------------------------------------------------------------------
# Treatment products catalogue (seeded into the `products` table).
# `tags` is the list of disease class names each product treats.
# ---------------------------------------------------------------------------
TREATMENT_PRODUCTS = [
    {
        "name_en": "Captan 50% WP Fungicide",
        "name_ar": "مبيد كابتان الفطري 50%",
        "price": 180.0,
        "desc_en": "Broad-spectrum protectant fungicide for scab, black rot and leaf scorch. Spray on a preventive schedule.",
        "desc_ar": "مبيد فطري وقائي واسع المدى لمكافحة الجرب والعفن الأسود ولفحة الأوراق. يُرش بنظام وقائي.",
        "image": _med("captan"),
        "tags": ["Apple Apple scab", "Apple Black rot", "Strawberry Leaf scorch"],
    },
    {
        "name_en": "Mancozeb 80% WP Fungicide",
        "name_ar": "مبيد مانكوزيب الفطري 80%",
        "price": 150.0,
        "desc_en": "Protectant contact fungicide for rusts, blights and leaf spots on many crops.",
        "desc_ar": "مبيد فطري وقائي بالملامسة لمكافحة الأصداء واللفحات وتبقعات الأوراق في محاصيل عديدة.",
        "image": _med("mancozeb"),
        "tags": [
            "Apple Apple scab", "Apple Cedar apple rust", "Corn (maize) Common rust",
            "Grape Black rot", "Grape Leaf blight (Isariopsis Leaf Spot)",
            "Potato Early blight", "Potato Late blight",
            "Tomato Early blight", "Tomato Late blight", "Tomato Septoria leaf spot",
        ],
    },
    {
        "name_en": "Myclobutanil Systemic Fungicide",
        "name_ar": "مبيد ميكلوبيوتانيل الجهازي",
        "price": 220.0,
        "desc_en": "Systemic triazole fungicide that controls powdery mildew, rust and black rot.",
        "desc_ar": "مبيد فطري جهازي من مجموعة التريازول يكافح البياض الدقيقي والصدأ والعفن الأسود.",
        "image": _med("myclobutanil"),
        "tags": [
            "Apple Apple scab", "Apple Cedar apple rust",
            "Cherry (including sour) Powdery mildew", "Grape Black rot",
            "Squash Powdery mildew",
        ],
    },
    {
        "name_en": "Copper Oxychloride Fungicide/Bactericide",
        "name_ar": "مبيد أوكسي كلورايد النحاس فطري/بكتيري",
        "price": 130.0,
        "desc_en": "Copper-based protectant controlling bacterial spot and several fungal blights and leaf molds.",
        "desc_ar": "مبيد نحاسي وقائي يكافح التبقع البكتيري والعديد من اللفحات الفطرية وعفن الأوراق.",
        "image": _med("copper_oxychloride"),
        "tags": [
            "Apple Black rot", "Grape Leaf blight (Isariopsis Leaf Spot)",
            "Peach Bacterial spot", "Pepper bell Bacterial spot",
            "Potato Late blight", "Strawberry Leaf scorch",
            "Tomato Bacterial spot", "Tomato Leaf Mold", "cotton Bacterial Blight",
        ],
    },
    {
        "name_en": "Wettable Sulfur 80%",
        "name_ar": "كبريت قابل للبلل 80%",
        "price": 90.0,
        "desc_en": "Sulfur dust/spray that controls powdery mildew and suppresses mites.",
        "desc_ar": "كبريت يُرش لمكافحة البياض الدقيقي والحد من الأكاروسات (العناكب).",
        "image": _med("sulfur"),
        "tags": [
            "Cherry (including sour) Powdery mildew", "Squash Powdery mildew",
            "cotton Powdery Mildew",
        ],
    },
    {
        "name_en": "Chlorothalonil Fungicide",
        "name_ar": "مبيد كلوروثالونيل الفطري",
        "price": 175.0,
        "desc_en": "Broad-spectrum protectant for early/late blight, leaf mold, Septoria and target spot.",
        "desc_ar": "مبيد وقائي واسع المدى للفحة المبكرة والمتأخرة وعفن الأوراق والسبتوريا وبقعة الهدف.",
        "image": _med("chlorothalonil"),
        "tags": [
            "Potato Early blight", "Potato Late blight",
            "Tomato Early blight", "Tomato Late blight", "Tomato Leaf Mold",
            "Tomato Septoria leaf spot", "Tomato Target Spot", "cotton Target spot",
        ],
    },
    {
        "name_en": "Azoxystrobin Fungicide",
        "name_ar": "مبيد أزوكسيستروبين الفطري",
        "price": 260.0,
        "desc_en": "Strobilurin systemic fungicide for gray leaf spot, northern leaf blight and target spot.",
        "desc_ar": "مبيد جهازي من مجموعة الستروبيلورين لتبقع الأوراق الرمادي ولفحة الأوراق الشمالية وبقعة الهدف.",
        "image": _med("azoxystrobin"),
        "tags": [
            "Corn (maize) Cercospora leaf spot Gray leaf spot",
            "Corn (maize) Northern Leaf Blight", "Tomato Target Spot",
            "cotton Target spot",
        ],
    },
    {
        "name_en": "Propiconazole Fungicide",
        "name_ar": "مبيد بروبيكونازول الفطري",
        "price": 240.0,
        "desc_en": "Systemic triazole fungicide for corn rust, gray leaf spot and northern leaf blight.",
        "desc_ar": "مبيد جهازي من التريازول لصدأ الذرة وتبقع الأوراق الرمادي ولفحة الأوراق الشمالية.",
        "image": _med("propiconazole"),
        "tags": [
            "Corn (maize) Cercospora leaf spot Gray leaf spot",
            "Corn (maize) Common rust", "Corn (maize) Northern Leaf Blight",
        ],
    },
    {
        "name_en": "Abamectin Miticide",
        "name_ar": "مبيد أبامكتين للأكاروسات",
        "price": 300.0,
        "desc_en": "Miticide/insecticide that controls two-spotted spider mites.",
        "desc_ar": "مبيد للأكاروسات والحشرات يكافح العنكبوت الأحمر ذي البقعتين.",
        "image": _med("abamectin"),
        "tags": ["Tomato Spider mites Two-spotted spider mite"],
    },
    {
        "name_en": "Insecticidal Soap / Horticultural Oil",
        "name_ar": "صابون حشري / زيت بستاني",
        "price": 85.0,
        "desc_en": "Soft, low-toxicity spray for mites and aphids; good for sensitive plants and pre-harvest.",
        "desc_ar": "رشة لطيفة منخفضة السمية للأكاروسات والمنّ؛ مناسبة للنباتات الحساسة وقبل الحصاد.",
        "image": _med("insecticidal_soap"),
        "tags": ["Tomato Spider mites Two-spotted spider mite", "cotton Aphids"],
    },
    {
        "name_en": "Imidacloprid Systemic Insecticide",
        "name_ar": "مبيد إيميداكلوبريد الجهازي",
        "price": 195.0,
        "desc_en": "Systemic insecticide to control whiteflies, psyllids and aphids that spread viruses and citrus greening.",
        "desc_ar": "مبيد جهازي لمكافحة الذباب الأبيض والبسيلا والمنّ الناقلة للفيروسات ومرض تخضير الحمضيات.",
        "image": _med("imidacloprid"),
        "tags": [
            "Orange Haunglongbing (Citrus greening)",
            "Tomato Tomato Yellow Leaf Curl Virus", "cotton Aphids",
        ],
    },
    {
        "name_en": "Spinosad Bio-Insecticide",
        "name_ar": "مبيد سبينوساد الحيوي",
        "price": 210.0,
        "desc_en": "Bio-insecticide effective against armyworm and other leaf-eating caterpillars.",
        "desc_ar": "مبيد حيوي فعّال ضد الدودة الجيشية واليرقات الأخرى التي تتغذى على الأوراق.",
        "image": _med("spinosad"),
        "tags": ["cotton Army worm"],
    },
    {
        "name_en": "Oxytetracycline Agricultural Bactericide",
        "name_ar": "مبيد أوكسي تتراسيكلين البكتيري الزراعي",
        "price": 230.0,
        "desc_en": "Agricultural antibiotic spray used with copper to manage bacterial spot on stone fruit.",
        "desc_ar": "مضاد حيوي زراعي يُرش مع النحاس لإدارة التبقع البكتيري في الفاكهة ذات النواة.",
        "image": _med("oxytetracycline"),
        "tags": ["Peach Bacterial spot"],
    },
    {
        "name_en": "Bordeaux Mixture (Copper + Lime)",
        "name_ar": "محلول بوردو (نحاس + جير)",
        "price": 120.0,
        "desc_en": "Classic protectant spray that limits secondary spread of Esca and other trunk/leaf fungi.",
        "desc_ar": "رشة وقائية كلاسيكية تحد من الانتشار الثانوي لمرض الإسكا وفطريات الجذع والأوراق الأخرى.",
        "image": _med("bordeaux"),
        "tags": ["Grape Esca (Black Measles)"],
    },
    {
        "name_en": "Farm Disinfectant & Tool Sanitizer",
        "name_ar": "مطهّر مزرعة ومعقّم أدوات",
        "price": 75.0,
        "desc_en": "Virucidal disinfectant for hands, tools and surfaces to stop contact-spread viruses like ToMV.",
        "desc_ar": "مطهّر مضاد للفيروسات لليدين والأدوات والأسطح لوقف الفيروسات المنتقلة باللمس مثل ToMV.",
        "image": _med("disinfectant"),
        "tags": ["Tomato Tomato mosaic virus"],
    },
]
