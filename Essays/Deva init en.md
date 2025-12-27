# Deva.init()

*Three months in Vilnius, five thousand years to home*

---

## I. Deploy

Vikram Sundaram, senior developer, Bangalore, twenty-nine years old.

Three months in Vilnius. Integration project for a Lithuanian fintech. Good rate, apartment covered, chance to see Europe. It'll be cold, but it's not like he hasn't worked with people from the other side of the world before.

Code is code. Same everywhere.

First week is exactly what he expected. Airport, taxi, apartment in the center. Office like every other office — open space, monitors, coffee from the machine, daily standup at ten. The Lithuanians are nice, a bit reserved, speak good English. Jira, Git, Slack. Could be Bangalore, Dublin, Singapore. Same everywhere.

"Hey dev, can you check this PR?"

Vikram nods. Dev. Short for developer. He hears this word fifty times a day. Says it himself. Normal.

Second week, the problem begins.

---

## II. Exception

Friday, team integration. Bar in the old town. Someone orders something in Lithuanian, Vikram catches fragments of conversation.

*"Dievas žino..."*

God knows.

Vikram stops with his glass halfway to his mouth.

*Dievas.*

He knows what the word means. It means *God* in Lithuanian, he's heard it a few times already. But this time — he doesn't know why — something in him halts.

He goes back to the hotel and can't sleep. At two in the morning he types into Google:

"dievas etymology"

And the world stops compiling.

---

## III. Stack Trace

*Dievas* — Lithuanian. God.

*Devas* — Sanskrit. Gods. Luminous beings.

The same word.

Vikram is a programmer. He understands patterns. Sees them in code, sees them in data, sees them in systems. One case is an accident. Two is coincidence.

Three is a pattern.

He starts searching.

---

| Lithuanian | Sanskrit | Meaning |
|------------|----------|---------|
| dievas | devas | god |
| ugnis | agni | fire |
| vyras | vīra | man/hero |
| sūnus | sūnu | son |
| avis | avi | sheep |
| vilkas | vṛka | wolf |
| naktis | nakti | night |
| duktė | duhitṛ | daughter |
| akmuo | aśman | stone |

Nine words. Then twenty. Then fifty.

At four in the morning Vikram sits on the bed with his laptop on his knees and a pattern he can't ignore.

*This isn't coincidence*, he thinks. *This is inheritance.*

---

## IV. Singleton

There's a design pattern Vikram knows by heart. Singleton. One instance of an object, shared across the entire system. You don't create a new one — you get a reference to the same, existing one.

```java
public class Deva {
    private static Deva instance;
    
    private Deva() {
        // created once, 5000 years ago
    }
    
    public static Deva getInstance() {
        if (instance == null) {
            instance = new Deva(); // Yamnaya, 3000 BCE
        }
        return instance;
    }
}
```

Lithuanian *dievas* and Sanskrit *devas* aren't two different words.

They're two references to the same singleton.

Created once. Five thousand years ago. On a steppe somewhere between Ukraine and Kazakhstan.

And Vikram — senior developer, Bangalore, twenty-nine years old — has just realized that his whole life he's been calling `Deva.getInstance()` without knowing that this instance has existed since the Bronze Age.

---

## V. Documentation

1786, Calcutta.

Sir William Jones, British judge, orientalist, polyglot. Studies Sanskrit with Brahmin scholars. And one day — Vikram reads this with growing shock — Jones delivers a speech to the Asiatic Society:

*"The Sanskrit language, whatever be its antiquity, is of a wonderful structure; more perfect than the Greek, more copious than the Latin, and more exquisitely refined than either, yet bearing to both of them a stronger affinity... than could possibly have been produced by accident; so strong indeed, that no philologer could examine them all three, without believing them to have sprung from some common source, which, perhaps, no longer exists."*

Common source.

Jones didn't know about Lithuanian yet. If he had, he would have lost his mind.

Because Lithuanian is closer to Sanskrit than Greek. Than Latin. Than anything else in Europe.

A Lithuanian peasant in the 19th century, who had never heard of India, could understand fragments of the Vedas.

---

## VI. Legacy Code

Vikram hasn't slept for three nights now.

On the screen he has a map. The Pontic-Caspian steppe. Ukraine, southern Russia, Kazakhstan. Five thousand years ago — the Yamnaya culture. Burial mounds. Horses. Wheels.

And a language. *Proto-Indo-European*. A language no one wrote down, because there was no writing yet. But which linguists *reconstructed* — word by word, sound by sound — from what remained in the descendant languages.

```
// Proto-Indo-European base class (3000 BCE)
*déywos → "celestial being, god"

// Inherited implementations:
Sanskrit: devas (देव)     // India branch
Lithuanian: dievas        // Baltic branch  
Latin: deus               // Italic branch
Old Norse: tívar          // Germanic branch
```

One tribe. One language. Then — divergence. Westward went the ancestors of the Celts, Germans, Italics, Greeks, Slavs. Eastward — the ancestors of the Persians, the Indians.

And somewhere in the middle, by the Baltic, Lithuania remained. Which *never did a major version update*.

---

## VII. Frozen Dependency

Languages evolve. That's natural. They lose cases, simplify grammar, change vocabulary. Latin had six cases — Italian has almost none. Sanskrit had eight — Hindi barely two.

Lithuanian has seven.

Lithuanian preserved *dual number* — a form for exactly two things, separate from singular and plural. Most Indo-European languages dropped this before Christ.

Lithuanian still has it.

Vikram thinks: *it's like finding a production server running code from five thousand years ago. No patches. No updates. And everything still works.*

Linguists call Lithuanian a "living fossil." Not because it's primitive. Because it's *faithful*.

Lithuania didn't *preserve* the ancestral language.

Lithuania simply *never refactored*.

---

## VIII. Disclaimer

Third night. Vikram is deep in the etymology rabbit hole now.

And he finds something that stops him.

He checks the word *developer*. Thinks — maybe there's a connection here too? Maybe *dev*, which he says fifty times a day, has some relationship to *deva*?

It doesn't.

*Developer* comes from Old French *desveloper* — "to unwrap, to unfold." From *des-* (undo) + *voloper* (wrap up). Completely different branch. No connection to Proto-Indo-European *\*déywos*.

Vikram sits and thinks.

And he understands something important: not everything connects. Not every similarity is real. Sometimes *dev* is just short for *developer*, and that's it. It would be easy — and tempting — to write that every programmer is a god without knowing it. Nice metaphor. False etymology.

But that doesn't change what *is* true.

*Ugnis* and *agni* — the same word. Fire.

*Dievas* and *devas* — the same word. God.

*Sūnus* and *sūnu* — the same word. Son.

You don't need to stretch etymology. The real connections are astonishing enough.

And there's something else. Vikram reads about Polish — a language he only knows from labels in Lithuanian shops — and finds the word *rękoma*. Instrumental dual. A fossil. A Pole says "with my own hands" (*własnymi rękoma*) not knowing they're using a grammatical form that most Indo-European languages dropped before Christ.

Lithuanian preserved the entire dual number. Polish preserved remnants — *rękoma*, *oczyma*, *uszyma*. Like fragments of code that was once a full module, now existing only in a few legacy functions that no one refactors because "it's always been that way."

*Truth is strange enough*, thinks Vikram. *You don't need to embellish it.*

---

## IX. Merge Conflict

Vikram goes to lunch with Jonas, the Lithuanian team lead. They sit in a restaurant in the old town, eating cepelinai.

"Jonas, can I ask you something?"

"Sure."

"Your word for God. *Dievas*. Do you know where it comes from?"

Jonas shrugs. "Old word. We've always said it."

"In Sanskrit — the ancient language of India — gods are *devas*. Same word."

Jonas stops eating.

"Same?"

"Same. And *ugnis* — fire. For us it's *agni*. And *sūnus* — son. For us it's *sūnu*. Dozens of words. Hundreds."

Jonas is silent for a long time.

"How do you know this?"

"Three nights without sleep and Wikipedia."

"And what does it mean?"

Vikram doesn't know how to answer. Because the answer is too big. The answer is that five thousand years ago his ancestors and Jonas's ancestors lived in the same place, spoke the same language, worshipped the same *devas*.

And then they parted — some east, through the mountains, to the Ganges valley; others north, through the forests, to the Baltic — and for five thousand years they knew nothing of each other.

Until now they sit in a restaurant in Vilnius, two programmers eating potatoes, and discover they're family.

"It means," Vikram finally says, "that your *dievas* and my *deva* are the same singleton. Initialized once, five thousand years ago. Still running."

Jonas doesn't understand the metaphor. But he understands something else.

"So we're... cousins?"

"Cousins with a five-thousand-year communication delay."

---

## X. System Architecture

There are things Vikram doesn't tell Jonas. Because he doesn't understand them himself yet.

But at night, in the hotel, he keeps reading. And finds something that changes everything.

The Yamnaya culture — that primordial Proto-Indo-European culture — had a specific social model. Archaeologists and linguists reconstruct it from burials, from mythology, from what remained in descendant languages.

Not conquest through annihilation. *Integration through marriage*.

Yamnaya clans didn't massacre their neighbors. They formed alliances. Women moved between groups, carrying with them language, songs, gods. Men from different clans became *kin* — not through blood, through *choice*.

This is the source code. The system architecture from five thousand years ago.

And Vikram suddenly sees how this same architecture replicates across millennia.

---

## XI. Fork

The Grand Duchy of Lithuania, 13th-16th century.

Vikram reads and doesn't believe his own eyes.

Because this *isn't* a normal medieval state. This is something strange. Something that doesn't fit the pattern.

The GDL didn't conquer through annihilation. It *integrated*. Ruthenia, Samogitia, Podolia, Volhynia — not "conquered territories." *Partners*. Each keeps its own language, its own law, its own faith.

The official language of the Grand Duchy of Lithuania wasn't Lithuanian. It was *Ruthenian* — an East Slavic language, ancestor of today's Belarusian and Ukrainian. Lithuanians ruled a state where *the majority spoke a different language*.

And it worked. For three hundred years.

How?

Vikram knows the answer. Because he's seen it before. In code from five thousand years ago.

*Integration through marriage. Through alliance. Through choice.*

Jagiełło didn't conquer Poland. He married Jadwiga. Union of Krewo, 1385. Two states become one not through the sword — through *merge*.

```
// 1385: Union of Krewo
Kingdom poland = Kingdom.getInstance("Poland");
GrandDuchy lithuania = GrandDuchy.getInstance("Lithuania");

// Not conquest. Marriage.
Union krewo = new Union(poland, lithuania, UnionType.PERSONAL);
krewo.merge();
```

1569, Union of Lublin. Not annexation. *The Commonwealth of Both Nations*. Lithuanian noble and Polish noble are equal. A Ruthenian can be hetman. A Tatar can be cavalry commander. An Armenian can be a merchant.

This is *pattern inheritance*. The same integration model that worked on the steppe in the Bronze Age works on the Baltic in the 16th century.

Code older than Rome. Still in production.

---

## XII. Runtime

There's something else.

Vikram reads about the First Polish Republic and finds a word that stops him.

*Liberum veto.*

Any deputy could block a law. Any single one. Regardless of how many were in favor.

Historians write that this destroyed Poland. That it was a system error. That it's why the state fell.

But Vikram is a programmer. And he sees something different.

He sees a *consensus protocol*.

In distributed systems there's something called Byzantine Fault Tolerance. For the system to work, everyone must agree. One objection blocks the operation.

Liberum veto is *exactly that*.

And the thing is — in small systems it works. In a tribe, in a clan, in a group of people who know and trust each other — forcing consensus is a *strength*, not a weakness.

The problem appears when the system grows. When you have thousands of deputies instead of twenty. When people don't know each other. When external actors with their own agendas get involved.

Then the consensus protocol becomes an attack vector.

The First Republic didn't fall because it had a bad system. It fell because it had a system designed for a different scale — for a small clan on the steppe, not for the largest state in Europe.

*Legacy code*, thinks Vikram. *Worked for five thousand years. But it didn't scale.*

---

## XIII. Deprecation

It's five in the morning. Vikram hasn't slept all night.

On the screen he has twenty tabs open. Yamnaya culture. Proto-Indo-European. Grand Duchy of Lithuania. Union of Lublin. Liberum veto. Partitions.

And he sees it now. The whole chain.

Five thousand years ago, on the steppe, someone invented a system. Integration through marriage. Consensus instead of conquest. *Kin* defined by choice, not by blood.

That system *worked*. That's why it spread. That's why those people — Vikram's ancestors and Jonas's ancestors — conquered half the world. From India to Iceland, from Portugal to Bengal.

But systems age. Context changes. What was strength becomes weakness.

A steppe clan could function on consensus. A Commonwealth with millions of citizens — couldn't.

And in 1795 the system crashed. Three neighbors — who didn't play by the same rules — tore the state apart.

*End of life*, thinks Vikram. *Deprecated. System shutdown.*

But...

But the code didn't disappear.

It hid. In language. In words people say without knowing what they mean. In *devs* and *dievai*, in *agni* and *ugnis*, in sons and daughters, in wolves and nights.

Vikram looks at the list of words on the screen. Lithuanian and Sanskrit. Two columns. The same words.

*Backup*, he thinks. *System crashed, but someone made a backup. In the most resilient medium that exists. In language. In grammar. In words that mothers say to children.*

And now — five thousand years later — Vikram sits in a hotel in Vilnius and reads that backup.

---

## XIV. Reboot

Sixth week. Vikram is a different person.

He walks through Vilnius and hears. Really hears.

*Ugnis* in a conversation about a fireplace — and he sees *agni*, the sacrificial fire from the Vedas.

*Dievas* in a curse — and he sees *devas*, the luminous beings from mythology.

*Sūnus* in a mother's conversation with her child — and he sees *sūnu*, the word his grandmother used to say to his father.

This isn't a foreign country.

This is a *backup copy of home*.

---

It's evening. Vikram sits in a bar with the team. Someone puts on music — Lithuanian folk songs, the group Sutartinės.

And suddenly — a woman's voice, old, rough — begins to sing:

*"Oi šermukšnio šermukšnio, kur tu augai tarp balių..."*

Oh rowan, rowan, where did you grow among the swamps...

Vikram doesn't understand the words. But he understands the *melody*. Understands the *structure*. Understands something he can't name.

Because it's the same structure he heard at home. In songs his grandmother sang in the kitchen. In mantras his father recited in the morning.

Not the same song. The same *grammar of song*.

The same way the voice rises and falls. The same way repetitions build meaning. The same way sorrow and joy interweave in a single phrase.

*Singleton*, thinks Vikram. *Same instance. For five thousand years.*

---

## XV. Return Statement

Last week. Project finished. Integration works. Deployment successful.

Vikram packs his suitcase.

Jonas comes to say goodbye.

"Will you miss Vilnius?"

"I will," says Vikram. And thinks: *but not the way you think. Not the city. The discovery I made here. The backup I found.*

"You know what's strangest?" says Jonas. "Since our conversation about *dievas* I started noticing... things. Words. Patterns. Things I didn't see before."

"The singleton initialized."

"What?"

"Nothing. Programmer joke."

But it's not a joke. It's the truth.

---

## XVI. Commit

Vilnius airport. Check-in. Boarding.

Vikram sits by the window. The plane taxis to the runway.

And he thinks:

*For twenty-nine years I was a programmer. Developer. A person who writes code, who solves problems, who looks for patterns.*

*I didn't know the biggest pattern is in the words I say every day. That when I say "mother" — mātā — I'm saying the same word as Jonas when he says "motina." That when my father said "son" — sūnu — he was saying the same word as a Lithuanian mother saying "sūnus."*

*I didn't know my ancestors and Jonas's ancestors sat by the same fire. Ugnis. Agni. The same singleton of fire.*

*I didn't know the system they built — integration through choice, not through blood — ran for millennia. And that its echo is still in the words we speak.*

The plane takes off. Vilnius disappears beneath the clouds.

Vikram closes his eyes and sees: the steppe, five thousand years ago. A fire. People sitting in a circle. Someone says a word — *\*déywos* — and everyone understands.

And then they stand up and walk in different directions across the world.

And for five thousand years they say the same word.

Not knowing about each other.

Until now.

---

## Epilog

Bangalore. Thirty-two degrees, eighty percent humidity.

Vikram sits with his grandmother on the veranda. Drinks tea. Tells her about Vilnius.

"And they say *dievas*," he says. "Exactly like our *deva*. Same word."

Grandmother listens. Nods.

"And their songs," Vikram continues. "They have the same structure as ours. Same way of repetition. Same rhythm."

Grandmother is silent for a long time. Then she says:

"Your grandfather always used to say that truth is one. Only the languages are different."

Vikram thinks about Jonas. About the song about the rowan tree. About words that connect Vilnius to Bangalore across five thousand years.

"Grandma," he says. "Do you know songs from your village? The old ones, the ones you sang to mom?"

"I do."

"Will you sing for me?"

Grandmother closes her eyes. And begins to sing.

The melody rises and falls. Repetitions build meaning. Sorrow and joy interweave in a single phrase.

Vikram listens.

And somewhere — at that same moment, eight thousand kilometers away — someone in Vilnius turns on the radio and hears:

*"Oi šermukšnio šermukšnio, kur tu augai tarp balių,*
*Ei ei ajajaj, kur tu augai tarp balių?"*

Same singleton.

Same instance.

`Deva.getInstance()`

Still running.

---

\vspace{2em}

\begin{center}
\textit{Oi šermukšnio šermukšnio, kur tu augai tarp balių,}\\
\textit{Ei ei ajajaj, kur tu augai tarp balių?}\\
\vspace{0.5em}
Oh rowan, rowan, where did you grow among the swamps,\\
Ei ei ajajaj, where did you grow among the swamps?\\
\vspace{1em}
— Lithuanian folk song, age unknown
\end{center}
