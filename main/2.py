from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk

# If you get an error uncomment this line and download the necessary libraries
#nltk.download()

text = """ 1.1 Historical Perspective and Materials Science
1.1.1 Historical Perspective
Materials are so important in the development of human civilization that the historians have identified early periods of civilization by the name of most significantly used material, e.g.: Stone Age, Bronze Age. This is just an observation made to showcase the importance of materials and their impact on human civilization. It is obvious that materials have affected and controlling a broad range of human activities through thousands of decades.
From the historical point of view, it can be said that human civilization started with Stone Age where people used only natural materials, like stone, clay, skin, and wood for the purposes like to make weapons, instruments, shelter, etc. Thus the sites of deposits for better quality stones became early colonies of human civilization. However, the increasing need for better quality tools brought forth exploration that led to Bronze Age, followed by Iron Age. When people found copper and how to make it harder by alloying, the Bronze Age started about 3000 BC. The use of iron and steel, a stronger material that gave advantage in wars started at about 1200 BC. Iron was abundant and thus availability is not limited to the affluent. This commonness of the material affected every person in many aspects, gaining the name democratic material. The next big step in human civilization was the discovery of a cheap process to make steel around 1850 AD, which enabled the railroads and the building of the modern infrastructure of the industrial world. One of the most significant features of the democratic material is that number of users just exploded. Thus there has been a need for human and material resources for centuries, which still going strong. It’s being said and agreed that we are presently in Space Age marked by many technological developments towards development materials resulting in
stronger and light materials like composites, electronic materials like semiconductors,
materials for space voyage like high temperature ceramics, biomaterials, etc.
In summary, materials constitute foundation of technology. The history of human
civilization evolved from the Stone Age to the Bronze Age, the Iron Age, the Steel Age,
and to the Space Age (contemporaneous with the Electronic Age). Each age is marked by
the advent of certain materials. The Iron Age brought tools and utensils. The Steel Age
brought railroads, instruments, and the Industrial Revolution. The Space Age brought the
materials for stronger and light structures (e.g., composite materials). The Electronic Age
brought semiconductors, and thus many varieties of electronic gadgets.
1.1.2 Materials Science
As engineering materials constitute foundation of technology, it’s not only necessary but
a must to understand how materials behave like they do and why they differ in properties.
This is only possible with the atomistic understanding allowed by quantum mechanics
that first explained atoms and then solids starting in the 1930s. The combination of
physics, chemistry, and the focus on the relationship between the properties of a material
and its microstructure is the domain of Materials Science. The development of this
science allowed designing materials and provided a knowledge base for the engineering
applications (Materials Engineering).
Important components of the subject Materials Science are structure, properties,
processing, and performance. A schematic interrelation between these four components is
shown in figure 1.1.
Structure
Properties Processing
Performance
Figure 1.1: Interrelation between four components of Materials Science.
1.2 Why Study Materials Science and Engineering? and Classification of Materials?
1.2.1 Why Study Materials Science and Engineering?
All engineers need to know about materials. Even the most "immaterial", like software or
system engineering depend on the development of new materials, which in turn alter the
economics, like software-hardware trade-offs. Increasing applications of system
engineering are in materials manufacturing (industrial engineering) and complex
environmental systems.
Innovation in engineering often means the clever use of a new material for a specific
application. For example: plastic containers in place of age-old metallic containers. It is
well learnt lesion that engineering disasters are frequently caused by the misuse of
materials. So it is vital that the professional engineer should know how to select materials
which best fit the demands of the design - economic and aesthetic demands, as well as
demands of strength and durability. Beforehand the designer must understand the
properties of materials, and their limitations. Thus it is very important that every engineer
must study and understand the concepts of Materials Science and Engineering. This
enables the engineer
• To select a material for a given use based on considerations of cost and
performance.
• To understand the limits of materials and the change of their properties with use.
• To be able to create a new material that will have some desirable properties.
• To be able to use the material for different application.
1.2.2 Classification of Materials
Like many other things, materials are classified in groups, so that our brain can handle
the complexity. One can classify them based on many criteria, for example crystal
structure (arrangement of atoms and bonds between them), or properties, or use. Metals,
Ceramics, Polymers, Composites, Semiconductors, and Biomaterials constitute the main
classes of present engineering materials.
Metals: These materials are characterized by high thermal and electrical conductivity;
strong yet deformable under applied mechanical loads; opaque to light (shiny if
polished). These characteristics are due to valence electrons that are detached from
atoms, and spread in an electron sea that glues the ions together, i.e. atoms are bound
together by metallic bonds and weaker van der Waalls forces. Pure metals are not good
enough for many applications, especially structural applications. Thus metals are used in
alloy form i.e. a metal mixed with another metal to improve the desired qualities. E.g.:
aluminum, steel, brass, gold.
Ceramics: These are inorganic compounds, and usually made either of oxides, carbides,
nitrides, or silicates of metals. Ceramics are typically partly crystalline and partly
amorphous. Atoms (ions often) in ceramic materials behave mostly like either positive or
negative ions, and are bound by very strong Coulomb forces between them. These
materials are characterized by very high strength under compression, low ductility;
usually insulators to heat and electricity. Examples: glass, porcelain, many minerals.
Polymers: Polymers in the form of thermo-plastics (nylon, polyethylene, polyvinyl
chloride, rubber, etc.) consist of molecules that have covalent bonding within each
molecule and van der Waals forces between them. Polymers in the form of thermo-sets
(e.g., epoxy, phenolics, etc.) consist of a network of covalent bonds. They are based on
H, C and other non-metallic elements. Polymers are amorphous, except for a minority of
thermoplastics. Due to the kind of bonding, polymers are typically electrical and thermal
insulators. However, conducting polymers can be obtained by doping, and conducting
polymer-matrix composites can be obtained by the use of conducting fillers. They
decompose at moderate temperatures (100 – 400 C), and are lightweight. Other properties
vary greatly.
Composite materials: Composite materials are multiphase materials obtained by
artificial combination of different materials to attain properties that the individual
components cannot attain. An example is a lightweight brake disc obtained by embedding
SiC particles in Al-alloy matrix. Another example is reinforced cement concrete, a
structural composite obtained by combining cement (the matrix, i.e., the binder, obtained
by a reaction known as hydration, between cement and water), sand (fine aggregate),
gravel (coarse aggregate), and, thick steel fibers. However, there are some natural
composites available in nature, for example – wood. In general, composites are classified
according to their matrix materials. The main classes of composites are metal-matrix,
polymer-matrix, and ceramic-matrix.
Semiconductors: Semiconductors are covalent in nature. Their atomic structure is
characterized by the highest occupied energy band (the valence band, where the valence
electrons reside energetically) full such that the energy gap between the top of the
valence band and the bottom of the empty energy band (the conduction band) is small
enough for some fraction of the valence electrons to be excited from the valence band to
the conduction band by thermal, optical, or other forms of energy. Their electrical
properties depend extremely strongly on minute proportions of contaminants. They are
usually doped in order to enhance electrical conductivity. They are used in the form of
single crystals without dislocations because grain boundaries and dislocations would
degrade electrical behavior. They are opaque to visible light but transparent to the
infrared. Examples: silicon (Si), germanium (Ge), and gallium arsenide (GaAs, a
compound semiconductor).
Biomaterials: These are any type material that can be used for replacement of damaged
or diseased human body parts. Primary requirement of these materials is that they must
be biocompatible with body tissues, and must not produce toxic substances. Other
important material factors are: ability to support forces; low friction, wear, density, and
cost; reproducibility. Typical applications involve heart valves, hip joints, dental
implants, intraocular lenses. Examples: Stainless steel, Co-28Cr-6Mo, Ti-6Al-4V, ultra
high molecular weight poly-ethelene, high purity dense Al-oxide, etc.
1.3 Advanced Materials, Future Materials, and Modern Materials needs
1.3.1 Advanced Materials
These are materials used in High-Tech devices those operate based on relatively intricate
and sophisticated principles (e.g. computers, air/space-crafts, electronic gadgets, etc.).
These materials are either traditional materials with enhanced properties or newly
developed materials with high-performance capabilities. Hence these are relatively
expensive. Typical applications: integrated circuits, lasers, LCDs, fiber optics, thermal
protection for space shuttle, etc. Examples: Metallic foams, inter-metallic compounds,
multi-component alloys, magnetic alloys, special ceramics and high temperature
materials, etc.
1.3.2 Future Materials
Group of new and state-of-the-art materials now being developed, and expected to have
significant influence on present-day technologies, especially in the fields of medicine,
manufacturing and defense. Smart/Intelligent material system consists some type of
sensor (detects an input) and an actuator (performs responsive and adaptive function).
Actuators may be called upon to change shape, position, natural frequency, mechanical
characteristics in response to changes in temperature, electric/magnetic fields, moisture,
pH, etc.
Four types of materials used as actuators: Shape memory alloys, Piezo-electric ceramics,
Magnetostrictive materials, Electro-/Magneto-rheological fluids. Materials / Devices used
as sensors: Optical fibers, Piezo-electric materials, Micro-electro-mechanical systems
(MEMS), etc.
Typical applications: By incorporating sensors, actuators and chip processors into system,
researchers are able to stimulate biological human-like behavior; Fibers for bridges,
buildings, and wood utility poles; They also help in fast moving and accurate robot parts,
high speed helicopter rotor blades; Actuators that control chatter in precision machine
tools; Small microelectronic circuits in machines ranging from computers to
photolithography prints; Health monitoring detecting the success or failure of a product.
1.3.3 Modern Materials needs
Though there has been tremendous progress over the decades in the field of materials
science and engineering, innovation of new technologies, and need for better
performances of existing technologies demands much more from the materials field.
More over it is evident that new materials/technologies are needed to be environmental
friendly. Some typical needs, thus, of modern materials needs are listed in the following:
• Engine efficiency increases at high temperatures: requires high temperature
structural materials
• Use of nuclear energy requires solving problem with residues, or advances in
nuclear waste processing.
• Hypersonic flight requires materials that are light, strong and resist high
temperatures.
• Optical communications require optical fibers that absorb light negligibly.
• Civil construction – materials for unbreakable windows.
• Structures: materials that are strong like metals and resist corrosion like plastics.
References """

stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.5 * average)):
		summary += " " + sentence

print(summary)