#!/usr/bin/env python3
"""Build MCGG Season 7.1 data files: commanders.json, equipment.json, meta_comps.json.
Sources: Mobile Legends Fandom wiki (MCGG commander pages), GrindNStrat equipment guide,
Moonton official S7 announcement, GameMarket S7.1 preview, BlueStacks tier list,
ARCTopup/MTE comp guides, MCGG creator videos (Sep 2026). Anything doubtful is
flagged unverified. Do not invent skill numbers.
"""
import json, os

PATCH = "Season 7.1 (Chrono Echoes)"
OUT = os.path.expanduser("~/workspace/magic-chess/data")

def skill(name, star, stype, desc, unverified=False):
    s = {"name": name, "unlock_star": star, "type": stype, "description": desc}
    if unverified:
        s["unverified"] = True
    return s

def unknown_skill(note):
    return skill("Unverified", 1, "passive",
                "Exact skill details for Season 7.1 are unverified. " + note,
                unverified=True)

def cmdr(cid, name, category, meta, skills, notes, unverified=False):
    return {"id": cid, "name": name, "category": category, "meta": meta,
            "unverified": unverified, "skills": skills, "notes": notes}

COMMANDERS = [
    # ---------------- COMBAT ----------------
    cmdr("bersi", "Bersi", "Combat", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Combat). Skills not verified for S7.1.",
         unverified=True),
    cmdr("dubi", "Dubi", "Combat", False, [
        skill("Dubi's Gift", 1, "passive",
              "Grants Fluffy's Rage. The carrier leaves behind a Fluffy whenever moved. "
              "Fluffy explodes, stunning enemies in the same row/column for 0.5s."),
        skill("Awaken! Dubi's Wrath", 2, "passive",
              "Enemies hit by Fluffy's explosion take 10% extra damage for 2s."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Dubi), fetched 2026-09-29."),
    cmdr("fanny", "Fanny", "Combat", False, [
        skill("Blade Dancer", 1, "passive",
              "The Hero Launcher completes after 13 rounds. The hero placed in it joins the battle."),
        skill("Heart of the Blade", 2, "passive",
              "The Hero Launcher now takes only 9 rounds, and the launched hero gains 40% HP."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Fanny), fetched 2026-09-29."),
    cmdr("johnson", "Johnson", "Combat", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Combat). Skills not verified for S7.1.",
         unverified=True),
    cmdr("layla", "Layla", "Combat", True, [
        skill("Hologram: Malefic Gun", 1, "passive",
              "Creates a hologram that attacks the nearest enemy every 2 seconds, "
              "dealing stage-scaled damage."),
        skill("Hologram: Destruction Rush", 2, "passive",
              "The hologram fires a piercing laser, dealing stage-scaled damage."),
    ], "Skill data from BlueStacks MCGG tier list guide (Feb 2025); Fandom wiki page "
       "inaccessible (403) on 2026-09-29. Consensus A-tier commander across sources.",
         unverified=True),
    cmdr("ling", "Ling", "Combat", False, [
        skill("Showdown", 1, "active",
              "Opens a 25-second Dueling Ring. The farthest enemy is dragged into the ring "
              "to duel an allied hero, with both sides restricted to basic attacks."),
        skill("Transcendent Stance", 2, "passive",
              "Winning a duel permanently grants 5% Physical Attack, stacking up to 15 times."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Ling), fetched 2026-09-29. "
       "Was S-tier in older tier lists but reportedly nerfed in Season 6; S7.1 standing unconfirmed."),
    cmdr("lukas", "Lukas", "Combat", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Combat). Skills not verified for S7.1.",
         unverified=True),
    cmdr("miya", "Miya", "Combat", False,
         [unknown_skill("Fandom wiki page inaccessible (403) on 2026-09-29.")],
         "Listed in Fandom wiki MCGG commander nav (Combat). Skills not verified for S7.1.",
         unverified=True),
    cmdr("pao", "Pao", "Combat", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Combat). Skills not verified for S7.1.",
         unverified=True),
    cmdr("wanwan", "Wanwan", "Combat", False, [
        skill("Reinforcement", 1, "passive",
              "After more than half of allied heroes die, attacks the nearest enemy 12 times, "
              "dealing stage-scaled physical damage."),
        skill("Tiger's Pounce", 2, "passive",
              "Increases the number of attacks to 20."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Wanwan), fetched 2026-09-29. "
       "Was S-tier in older tier lists but reportedly nerfed; S7.1 standing unconfirmed."),
    cmdr("yuki", "Yuki", "Combat", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Combat). Skills not verified for S7.1.",
         unverified=True),
    cmdr("zilong", "Zilong", "Combat", True, [
        skill("Great Dragon Spear", 1, "passive",
              "Starts with a spear. Basic attacks have an 18% chance to attack twice additionally. "
              "Can buy one enhancement for the spear."),
        skill("Dragon's Roar", 2, "passive",
              "Can buy two additional enhancements for the spear."),
    ], "Skill data from BlueStacks MCGG tier list guide (Feb 2025). An advance-server video "
       "describes a Season 7 rework giving Zilong a brand-new trait-selection mechanic, so these "
       "skills may be outdated for S7.1. Used in the current S7 Bruiser + Dragon Altar comp.",
         unverified=True),
]

COMMANDERS += [
    # ---------------- SURVIVAL ----------------
    cmdr("abe", "Abe", "Survival", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Survival). Skills not verified for S7.1.",
         unverified=True),
    cmdr("angela", "Angela", "Survival", False, [
        skill("Love's Protection", 1, "passive",
              "Raises the selected ally's mana regeneration to 170% and grants a 20% Max HP shield."),
        skill("Ripples of Love", 2, "passive",
              "Protects one extra highest-power hero."),
    ], "Skill data from an older guide; Fandom wiki page inaccessible (403) on 2026-09-29. "
       "A 2026 advance-server video describes Angela as revamped with a 65% instant mana boost, "
       "so these old skills are likely outdated for S7.1.",
         unverified=True),
    cmdr("harper", "Harper", "Survival", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Survival). Skills not verified for S7.1.",
         unverified=True),
    cmdr("kagura", "Kagura", "Survival", True, [
        skill("Shield Umbrella", 1, "passive",
              "The Yin-Yang Umbrella grants allied heroes a 9% Max HP shield every 10 seconds "
              "and restores a fixed amount of mana per second."),
        skill("Yin Yang Gathering", 2, "passive",
              "The shield granted by the umbrella increases to 18% Max HP."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Kagura), fetched 2026-09-29. "
       "S-tier in older tier lists."),
    cmdr("mavis", "Mavis", "Survival", False, [
        skill("Gathering Strength", 1, "passive",
              "Since the Showdown Stage, each round win regenerates 8 HP."),
        skill("A Matter of Life or Death", 2, "passive",
              "Regenerates 8 HP whenever a commander is eliminated; increased to 28 HP if the "
              "commander was eliminated by you."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Mavis), fetched 2026-09-29. "
       "Numbers differ from older guides (which cited 2 HP per win); wiki values used. "
       "Was S-tier in older tier lists; S7.1 standing unconfirmed."),
    cmdr("nana", "Nana", "Survival", True, [
        skill("Molina's Blessing", 1, "passive",
              "Avoids the first death: stays at 1 HP and receives an equipment chest."),
        skill("Molina's Gift", 2, "passive",
              "The first damage taken grants 6 gold."),
    ], "Skill data from BlueStacks MCGG tier list guide (Feb 2025); Fandom wiki page "
       "inaccessible (403) on 2026-09-29. Dependable A-tier commander across sources and used "
       "in current S7 comps (Echomancer + Scavenger, 6 Stargazer 3 Necrokeep).",
         unverified=True),
    cmdr("ragnar", "Ragnar", "Survival", False, [
        skill("Unverified", 1, "passive",
              "Ragnar restores 7 HP immediately.", unverified=True),
        skill("Unverified", 1, "passive",
              "Ragnar reduces the damage received in the current round by 50%.",
              unverified=True),
    ], "Effects from Mobile Legends Fandom wiki (MCGG:Ragnar), fetched 2026-09-29; the wiki "
       "page uses template placeholders so the exact skill names are unknown. A new S7 commander "
       "Franco is reported to replace Ragnar. Availability in S7.1 unconfirmed.",
         unverified=True),
    cmdr("franco", "Franco", "Survival", False,
         [unknown_skill("Reported as a new S7 commander replacing Ragnar; exact skills not found.")],
         "New commander in Season 7, reported to replace Ragnar (advance-server coverage, "
         "Aug-Sep 2026). Creator videos show fast level-10 play after a buff. Exact skills "
         "unverified for S7.1.",
         unverified=True),
    # ---------------- RESOURCE ----------------
    cmdr("asta", "Asta", "Resource", False,
         [unknown_skill("No accessible Season 7.1 skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Resource). Skills not verified for S7.1.",
         unverified=True),
    cmdr("chou", "Chou", "Resource", True, [
        skill("Warrior's Honor", 1, "passive",
              "Gain 1 gold after winning a round."),
        skill("Win or Lose", 2, "passive",
              "When you lose a round, gain 2 gold, with a 30% chance to receive 1 extra gold."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Chou), fetched 2026-09-29. "
       "Used in current S7 Shadeweaver + Starbelle comp and the 6 Dragon Altar 4 Swordsman comp."),
    cmdr("guinevere", "Guinevere", "Resource", True, [
        skill("Super Magic", 1, "passive",
              "When refreshing the shop, there is a 14% chance to find 1 free hero."),
        skill("Mystic Evolution", 2, "passive",
              "The chance of finding free heroes increases to 26%."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Guinevere), fetched 2026-09-29. "
       "Recommended as a current S7 economy commander for the 6 Kishin comp."),
    cmdr("lancelot", "Lancelot", "Resource", False, [
        skill("Golden Legacy", 1, "passive",
              "No longer earns interest. Starting from Stage I/II/III onward, gain 2/2/3 bonus "
              "gold each round. At the end of each round, all gold is consumed to upgrade Lancelot."),
        skill("Golden Blade", 2, "passive",
              "From Stage I/II/III onward, the bonus gold increases to 2/3/4."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Lancelot), fetched 2026-09-29."),
    cmdr("popol-and-kupa", "Popol and Kupa", "Resource", True,
         [unknown_skill("No accessible Season 7.1 commander skill source found.")],
         "Listed in Fandom wiki MCGG commander nav (Resource). Recommended as a current S7 "
         "economy commander for the 6 Kishin comp. Exact skills unverified for S7.1.",
         unverified=True),
]

COMMANDERS += [
    # ---------------- STRATEGY ----------------
    cmdr("aamon", "Aamon", "Strategy", False, [
        skill("Blade of Resonance", 1, "passive",
              "Each 2-star hero grants one Shard. Collecting 7 Shards creates a Mirror Device. "
              "Up to 3 Mirror Devices can be held."),
        skill("Skybreaker Blade", 2, "passive",
              "Gain 8 gold whenever a Mirror Device is created."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Aamon), fetched 2026-09-29."),
    cmdr("aurora", "Aurora", "Strategy", False, [
        skill("Frost Treasures", 1, "passive",
              "The shop freezes each round. Buying no heroes grants 2 Frost Energy; at 6 Frost "
              "Energy, gain a random reward worth at least 5 gold, then Frost Energy resets."),
        skill("Icy Blessing", 2, "passive",
              "Keeping the shop frozen in consecutive rounds increases the next Frost Energy gain to 3."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Aurora), fetched 2026-09-29."),
    cmdr("connie", "Connie", "Strategy", False, [
        skill("I Want All of Them!", 1, "passive",
              "During Go Go Box rounds 2 and 3, after the selections, choose one extra unselected hero."),
        skill("Unrestricted", 2, "passive",
              "The extra selection can also include Equipment and Magic Crystals."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Connie), fetched 2026-09-29."),
    cmdr("eggie", "Eggie", "Strategy", False,
         [unknown_skill("Fandom wiki page inaccessible (403) on 2026-09-29.")],
         "Listed in Fandom wiki MCGG commander nav (Strategy). Skills not verified for S7.1.",
         unverified=True),
    cmdr("eva", "Eva", "Strategy", False, [
        skill("Blessing", 1, "passive",
              "With at least one active synergy count of 6 or higher, all allied heroes gain "
              "10% Hybrid ATK."),
        skill("Supplication", 2, "passive",
              "If exactly one synergy of 6 or higher is active and no others, all allied heroes "
              "gain 8% Attack Speed instead."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Eva), fetched 2026-09-29."),
    cmdr("harley", "Harley", "Strategy", False,
         [unknown_skill("Fandom wiki page inaccessible (403) on 2026-09-29.")],
         "Listed in Fandom wiki MCGG commander nav (Strategy). Skills not verified for S7.1.",
         unverified=True),
    cmdr("lunox", "Lunox", "Strategy", False, [
        skill("Budding Blossom", 1, "active",
              "Usable after Stage III. Select a hero without a Blessing to grant them a random "
              "Blessing. Can be used 1 time. (Blessing: the blessed hero contributes +1 to their "
              "Role or Faction Synergy.)"),
        skill("Dawn's Gift", 2, "passive",
              "Unlocks after Stage II.", unverified=True),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Lunox), fetched 2026-09-29. The wiki page does "
       "not document Dawn's Gift's effect text, so its description is unverified."),
    cmdr("lylia", "Lylia", "Strategy", True, [
        skill("Little Witch's Shop", 1, "active",
              "Revamped skill in Season 7.1: freely choose heroes at Commander Level 8; bonus "
              "shop access tied to collection milestones (preview shows 8/8).", unverified=True),
        skill("Unverified", 2, "passive",
              "Second skill / second-star upgrade details not confirmed for S7.1.",
              unverified=True),
    ], "S7.1 revamp confirmed by official app changelog ('Revamped Commander Lylia returns with "
       "\"Little Witch's Shop\"! Freely choose Heroes at Lv.8.') and GameMarket S7.1 preview "
       "(2026-09-09). The Fandom wiki page still shows pre-revamp Tharz-era skills and is stale. "
       "Exact mechanics beyond the Level-8 hero choice are unverified.",
         unverified=True),
    cmdr("moskov", "Moskov", "Strategy", True, [
        skill("Power of Shadow", 1, "passive",
              "Sacrifice the designated 1/2/3/4-cost heroes in the Shadow Field; the next hero "
              "gains 18% Hybrid ATK and 18% HP. The sacrificed heroes' sale value is refunded."),
        skill("Dark Star", 2, "passive",
              "Creates two additional 1-star copies of the enhanced hero."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Moskov), fetched 2026-09-29. "
       "Consensus A-tier commander across sources."),
    cmdr("vale", "Vale", "Strategy", False, [
        skill("Updraft", 1, "active",
              "Choose a hero, then refresh the shop to show only heroes sharing at least one "
              "synergy with it; one purchase is free. Charges available at Stage I-1 and Stage III-1."),
        skill("Shifting Wind", 2, "passive",
              "Grants an additional use of Updraft at Stage III-1."),
    ], "Source: Mobile Legends Fandom wiki (MCGG:Vale), fetched 2026-09-29. "
       "Received adjustments in Season 6."),
    cmdr("brody", "Brody", "Strategy", False, [
        skill("Abyss Domain", 1, "active",
              "New Season 7.1 signature mechanic: the Abyss Domain assesses heroes based on their "
              "costs and synergies, supporting synergy-completion play.", unverified=True),
        skill("Unverified", 2, "passive",
              "Second skill / second-star upgrade details not confirmed for S7.1.",
              unverified=True),
    ], "New commander added in Season 7.1 (launched 2026-09-09), confirmed by GameMarket S7.1 "
       "preview and official app changelog ('The Abyss Domain assesses Heroes based on their "
       "costs and Synergies.'). Exact skill names and full mechanics unverified.",
         unverified=True),
    # ---------------- ADDED AFTER WIKI NAV / UNCATEGORIZED ----------------
    cmdr("alice", "Alice", "Unknown", False,
         [unknown_skill("Added around January 2026 per update coverage; exact skills not found.")],
         "Commander added by January 2026 per MCGG update coverage. Wiki trivia on Mavis calls "
         "Alice her counterpart. Exact skills and category unverified for S7.1.",
         unverified=True),
    cmdr("diggie", "Diggie", "Unknown", False,
         [unknown_skill("Added around Season 5 per advance-server patch coverage.")],
         "Commander added around Season 5 per advance-server patch-note coverage, which mentions "
         "trade-offs for Diggie in Go Go Box rounds. Exact skills and category unverified.",
         unverified=True),
    cmdr("vexana", "Vexana", "Unknown", False,
         [unknown_skill("Added around Season 5; advance-server coverage mentions a huge gold buff.")],
         "Commander added around Season 5; advance-server patch coverage mentions a huge gold "
         "buff for Vexana. Exact skills and category unverified for S7.1.",
         unverified=True),
    cmdr("kalea", "Kalea", "Unknown", True,
         [skill("Treasure Trove", 1, "active",
                "High-risk, high-reward point system: stack points through play, then cash out "
                "for gold and hero rewards. A key mistake resets progress to zero.",
                unverified=True),
          skill("Unverified", 2, "passive",
                "Second skill / second-star upgrade details not confirmed for S7.1.",
                unverified=True)],
         "Commander added ~Season 6 (July 2026). Ability details from MCGG creator guide videos "
         "('Kalea's Treasure Trove ability, point system, cash out for gold and heroes'). "
         "Recommended economy commander in current S7 guides and used in the Dragoncaller + "
         "Dragon Altar comp. Exact names/numbers unverified.",
         unverified=True),
    cmdr("ruby", "Ruby", "Unknown", False,
         [unknown_skill("Added around July 2026 per update coverage; exact skills not found.")],
         "Commander added around July 2026 per MCGG update coverage. Exact skills and category "
         "unverified for S7.1.",
         unverified=True),
    cmdr("karina", "Karina", "Unknown", False, [
        skill("Shadow Twinblades", 1, "passive",
              "Gain Shadow Twinblades at the start of the game. When an enemy hero adjacent to "
              "the carrier has HP below 15%, Karina executes the target."),
        skill("Twinblades Evolution", 2, "passive",
              "After Karina executes a target, the carrier's DMG is increased by 1%, up to 35%."),
    ], "Skill data from Mobile Legends Fandom wiki page 'Karina (Magic Chess: GO GO)', which "
       "explicitly describes her as a commander (fetched via search snippet, 2026-09-29). She is "
       "absent from the wiki's commander nav list, so S7.1 roster availability is unverified.",
         unverified=True),
    cmdr("valir", "Valir", "Unknown", False,
         [unknown_skill("Named in advance-server commander-adjustment coverage and S7 guide videos.")],
         "Appears in S7 advance-server commander-adjustment coverage (Power Card reworks) and "
         "dedicated 'Master Valir Commander' S7 guide videos. Exact skills, category, and live "
         "roster status unverified for S7.1.",
         unverified=True),
    cmdr("luo-yi", "Luo Yi", "Unknown", True,
         [unknown_skill("Named as the commander for the S7 Starbelle + Scavenger comp in creator videos.")],
         "Named as the recommended commander for the current S7 'Starbelle + Scavenger' comp in "
         "MCGG creator videos. Exact skills, category, and roster status unverified for S7.1.",
         unverified=True),
]

# ---------------- EQUIPMENT ----------------
def equip(eid, name, category, effect, unverified=False, notes=""):
    e = {"id": eid, "name": name, "category": category, "effect": effect,
         "unverified": unverified}
    if notes:
        e["notes"] = notes
    return e

EQUIPMENT = [
    # Physical (source: GrindNStrat MCGG equipment guide)
    equip("demon-hunter", "Demon Hunter", "Physical",
          "Tank killer: deals bonus damage based on the target's max HP.",
          notes="MTE comp guides call it 'Demon Hunter Sword'; the equipment guide names it "
                "'Demon Hunter'. Naming discrepancy flagged."),
    equip("rose-gold-meteor", "Rose Gold Meteor", "Physical",
          "Grants bonus attack and a shield when the carrier drops to low HP."),
    equip("blade-of-despair", "Blade of Despair", "Physical",
          "Executes low-HP enemies: deals massive bonus damage to / finishes off weakened targets."),
    equip("golden-staff", "Golden Staff", "Physical",
          "Continuously increases the carrier's attack speed (stacking attack-speed effect)."),
    equip("sea-halberd", "Sea Halberd", "Physical",
          "Counters lifesteal (applies healing reduction) and provides high penetration."),
    equip("haas-claws", "Haas' Claws", "Physical",
          "Grants additional lifesteal on attacks."),
    equip("war-axe", "War Axe", "Physical",
          "Grants spell vamp (heals from skill damage dealt)."),
    equip("berserkers-fury", "Berserker's Fury", "Physical",
          "Increases the carrier's critical hit capability."),
    # Magic
    equip("enchanted-talisman", "Enchanted Talisman", "Magic",
          "Restores mana at the start of battle."),
    equip("glowing-wand", "Glowing Wand", "Magic",
          "Deals sustained magic damage over time and reduces enemy healing."),
    equip("feline-blade", "Feline Blade", "Magic",
          "Transforms an enemy at the start of battle or when damage conditions are met."),
    equip("winter-crown", "Winter Crown", "Magic",
          "Makes the carrier invincible at low HP (brief stasis/freeze)."),
    equip("ice-queen-wand", "Ice Queen Wand", "Magic",
          "Grants spell vamp (heals from magic skill damage dealt)."),
    equip("feather-of-heaven", "Feather of Heaven", "Magic",
          "Grants additional lifesteal."),
    equip("blood-wings", "Blood Wings", "Magic",
          "Periodically grants the carrier a shield."),
    # Defense
    equip("blade-armor", "Blade Armor", "Defense",
          "Reflects physical damage back at attackers."),
    equip("immortality", "Immortality", "Defense",
          "Resurrects the carrier on death with a portion of HP."),
    equip("dominance-ice", "Dominance Ice", "Defense",
          "Grants more mana regeneration when the carrier takes damage."),
    equip("guardian-helmet", "Guardian Helmet", "Defense",
          "Provides high base HP."),
    equip("brute-force-breastplate", "Brute Force Breastplate", "Defense",
          "Grants attack speed and crowd-control reduction."),
    equip("antique-cuirass", "Antique Cuirass", "Defense",
          "Reduces the target's hybrid attack."),
    equip("oracle", "Oracle", "Defense",
          "Increases allied heroes' hybrid defense."),
    # Special
    equip("mirror-device", "Mirror Device", "Special",
          "Clones the equipped hero (also created by Aamon's Blade of Resonance)."),
    equip("claudes-theft", "Claude's Theft", "Special",
          "Grants two random equipment at the beginning of the game."),
    equip("inspire", "Inspire", "Special",
          "Increases attack speed."),
    equip("knowledge-crystal", "Knowledge Crystal", "Special",
          "Upgrades the Erudition synergy."),
    equip("great-dragon-spear", "Great Dragon Spear", "Special",
          "Enhanceable Heavenly Artifact; used by Commander Zilong.",
          notes="Same name as Zilong's commander skill artifact."),
    equip("revitalize", "Revitalize", "Special",
          "Restores HP when the carrier drops to low HP."),
    equip("purify", "Purify", "Special",
          "Grants control immunity at the start of battle."),
    equip("flicker", "Flicker", "Special",
          "Blinks at the start of battle and grants attack speed."),
    equip("sunset-shield", "Sunset Shield", "Special",
          "Deals area-of-effect damage."),
    equip("aegis", "Aegis", "Special",
          "Shields allied heroes."),
    equip("retribution", "Retribution", "Special",
          "Kills level up the carrier and increase its damage."),
    equip("hunting-revolver", "Hunting Revolver", "Special",
          "Attacks can trigger an explosion."),
    equip("sun-staff", "Sun Staff", "Special",
          "Skills trigger an extra magic explosion."),
    # Legacy Magic Crystals (stale list from an older guide; S7 uses Choice Magic Crystal)
    equip("mc-dauntless", "Dauntless", "Magic Crystal",
          "Legacy Magic Crystal entry.", unverified=True,
          notes="From an older guide's Magic Crystal list (pre-S7). Season 7 uses the upgraded "
                "Choice Magic Crystal system per official Moonton announcement; this legacy list "
                "may not reflect the S7.1 crystal pool."),
    equip("mc-defender", "Defender", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-weapon-master", "Weapon Master", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-marksman", "Marksman", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-mage", "Mage", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-stargazer", "Stargazer", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-swordsman", "Swordsman", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-moniyan", "Moniyan", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-northern-vale", "Northern Vale", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-go-go", "Go Go", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-dragon-altar", "Dragon Altar", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-nature-spirit", "Nature Spirit", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-astro-power", "Astro Power", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-erudito", "Erudito", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-abyss", "Abyss", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
    equip("mc-los-pecados", "Los Pecados", "Magic Crystal", "Legacy Magic Crystal entry.",
          unverified=True, notes="Legacy pre-S7 Magic Crystal; S7.1 pool unconfirmed."),
]

# ---------------- META COMPS ----------------
MECHANICS = {
    "blessing": {
        "description": "A hero with a Blessing contributes +1 to their Role or Faction Synergy.",
        "source": "Mobile Legends Fandom wiki (MCGG:Lunox), fetched 2026-09-29",
        "unverified": False,
    },
    "shop_interest": {
        "description": "Hold 10-50 gold to earn interest each round. Typical level pacing: "
                       "level 4 by round 6, level 5 by round 9, level 6 by round 13, "
                       "level 7 by round 17, levels 8/9 around round 21+. Shop Lock preserves "
                       "the current shop heroes for the next round.",
        "source": "Current MCGG guide (ARCTopup), fetched 2026-09-29",
        "unverified": True,
    },
    "fate_box": {
        "description": "An extra board slot can be obtained from the Fate Box (Go Go Box).",
        "source": "Current MCGG guide, fetched 2026-09-29",
        "unverified": True,
    },
    "board_capacity": {
        "description": "Commander level determines deployable heroes: level 3 -> 3, 4 -> 4, "
                       "5 -> 5, 6 -> 6, 7 -> 7, 8 -> 8, 9 -> 9.",
        "slots_by_commander_level": {"3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9},
        "source": "Provided by requester; standard MCGG capacity rules",
        "unverified": False,
    },
    "choice_magic_crystal": {
        "description": "Season 7 introduced an upgraded Choice Magic Crystal system. Example: "
                       "assign a Choice Magic Crystal to Kishin to activate the 6-Kishin synergy. "
                       "Full selection mechanics unconfirmed.",
        "source": "Official Moonton S7 announcement (en.moonton.com/news/364.html); Kishin comp guide",
        "unverified": True,
    },
    "new_s7_synergies": {
        "description": "Season 7 added Echomancer (summons a random 5-cost hero from a past season), "
                       "SPECTRE (can unlock Alpha, MCGG's first 7-gold hero), Starbelle (Lightstick "
                       "turns a hero into a Fan), and Mistbender (gathers tokens during battle to "
                       "spend in a special shop). Dragon Altar and Shadeweaver returned.",
        "source": "Official Moonton S7 announcement (en.moonton.com/news/364.html)",
        "unverified": False,
    },
}

def comp(cid, name, patch, synergies, core_heroes, carry, items, commander,
         early_game, unverified=False, notes="", custom_brew=False):
    return {"id": cid, "name": name, "patch": patch, "synergies": synergies,
            "core_heroes": core_heroes, "carry": carry, "items": items,
            "commander": commander, "early_game": early_game,
            "unverified": unverified, "notes": notes, "custom_brew": custom_brew}

COMPS = [
    comp("kishin-phasewarper-shadeweaver", "6 Kishin 3 Phasewarper 3 Shadeweaver",
         PATCH, ["Kishin", "Phasewarper", "Shadeweaver", "Echomancer", "Scavenger"],
         ["Angela", "Franco", "Lunox", "Karrie", "Lancelot", "Thamuz", "Harley",
          "Kadita", "Melissa"],
         "", [],
         "Kalea",
         "Economy commander (Kalea, Guinevere, or Popol and Kupa). Early game: run "
         "Echomancer, Scavenger, and Phasewarper units while leveling to 9, then transition. "
         "Assign a Choice Magic Crystal to Kishin to activate 6 Kishin. Add Hylos for 3 "
         "Shadeweaver if a Fate Box slot or level 10 allows; if the Chrono Wanderer is "
         "Gatotkaca, replace Angela with Dyrroth.",
         unverified=True,
         notes="From a current S7 Kishin comp guide. Carry hero and item sets not specified in "
               "the source, so they are left empty rather than invented."),
    comp("stargazer-necrokeep", "6 Stargazer 3 Necrokeep",
         "S6/S7", ["Stargazer", "Necrokeep"],
         ["Minotaur", "Leomord", "Mathilda", "Lunox", "Chang'e", "Natan", "Aurora",
          "Yve", "Vexana", "Faramis"],
         "Vexana", ["Glowing Wand", "Enchanted Talisman", "Ice Queen Wand"],
         "Nana",
         "Prioritize the Stargazer Magic Crystal and EXP cards to hit power spikes early.",
         unverified=True,
         notes="From MTE's MCGG synergy/lineup guide. Predates Season 7.1; viability in the "
               "current patch is unconfirmed. Tank: Leomord with Demon Hunter Sword, Haas' Claws, "
               "Golden Staff."),
    comp("dragon-altar-swordsman", "6 Dragon Altar 4 Swordsman",
         "S6/S7", ["Dragon Altar", "Swordsman"],
         ["Ling", "Sun Wukong", "Lancelot", "Nolan", "Karina", "Wanwan", "Yin",
          "Chang'e", "Akai"],
         "Ling", ["Blade of Despair", "War Axe", "Winter Crown"],
         "Chou",
         "Take Inspire early for attack speed while building the Dragon Altar core.",
         unverified=True,
         notes="From MTE's MCGG synergy/lineup guide. Predates Season 7.1; viability in the "
               "current patch is unconfirmed. Tank: Sun Wukong with Dominance Ice, Immortality, Oracle."),
    comp("echomancer-scavenger", "Echomancer + Scavenger",
         PATCH, ["Echomancer", "Scavenger"],
         [], "", [], "Nana",
         "Strong Scavenger early game for economy and tempo; scales into a strong late game "
         "once a 3-star hero is online.",
         unverified=True,
         notes="From current S7 creator videos (top-global style Echomancer + Scavenger games). "
               "Exact hero board and item sets not specified in the source."),
    comp("bruiser-dragon-altar", "Bruiser + Dragon Altar",
         PATCH, ["Bruiser", "Dragon Altar", "Echomancer"],
         [], "", [], "Zilong",
         "Open with Echomancer units early, then pivot into the Bruiser + Dragon Altar core.",
         unverified=True,
         notes="From current S7 creator videos. Exact hero board and item sets not specified."),
    comp("dragoncaller-dragon-altar", "Dragoncaller + Dragon Altar",
         PATCH, ["Dragoncaller", "Dragon Altar", "Scavenger"],
         [], "", [], "Kalea",
         "Use Scavenger for a strong early game, then scale into the Dragoncaller + Dragon "
         "Altar late-game combo once a 3-star hero is online.",
         unverified=True,
         notes="From current S7 creator videos (Kalea commander). Exact hero board and item "
               "sets not specified."),
    comp("shadeweaver-starbelle", "Shadeweaver + Starbelle",
         PATCH, ["Shadeweaver", "Starbelle", "Scavenger"],
         [], "", [], "Chou",
         "Use Scavenger early for economy while assembling the Shadeweaver + Starbelle core.",
         unverified=True,
         notes="From current S7 creator videos (Chou commander). Exact hero board and item "
               "sets not specified."),
    comp("starbelle-scavenger", "Starbelle + Scavenger",
         PATCH, ["Starbelle", "Scavenger"],
         [], "", [], "Luo Yi",
         "Scavenger start for economy; transition into the Starbelle core.",
         unverified=True,
         notes="From current S7 creator videos (Luo Yi commander). Exact hero board and item "
               "sets not specified."),
    # ---- Racikan Jewel (custom brews, bukan meta komunitas) ----
    comp("jewel-lubang-bruiser", "6 Bruiser 2 Weapon Master (Racikan 🧪)",
         PATCH, ["Bruiser", "Weapon Master"],
         ["Dyrroth", "Belerick", "Martis", "Aldous", "Paquito", "Yin", "Suyou", "Badang"],
         "Badang", ["Golden Staff", "Haas' Claws", "Demon Hunter Sword"],
         "Franco",
         "Early: Dyrroth + Belerick + Martis, hemat gold, jangan roll. Mid (lv 6-7): lengkapkan "
         "4 Bruiser, cari Bintang 2. Late (lv 8): 6 Bruiser + 2 Weapon Master; Bintang 3-kan hero "
         "murah (Dyrroth, Belerick, Paquito). Item attack speed + lifesteal ke Badang/Yin, item "
         "tank (Dominance Ice, Immortality) ke Belerick/Aldous. Posisi: gerombol di tengah, adu pukul.",
         unverified=True, custom_brew=True,
         notes="Racikan Jewel: comp full-melee out-of-the-box. Bruiser proc double-strike + lifesteal "
               "satu tim = sustain adu pukul. Sepi kontes hero = gampang Bintang 3. Belum teruji di rank, "
               "coba di casual dulu."),
    comp("jewel-benteng-campuran", "4 Dauntless 2 Marksman 2 Mage (Racikan 🧪)",
         PATCH, ["Dauntless", "Marksman", "Mage"],
         ["Minotaur", "Balmond", "Miya", "Zhuxin", "Hilda", "Wanwan", "Kadita", "Lolita"],
         "Wanwan", ["Golden Staff", "Glowing Wand", "Enchanted Talisman"],
         "Guinevere",
         "Hemat early, roll di lv 7-8 untuk Bintang 2 semua. Item tank ke Lolita/Hilda; item attack "
         "speed ke Miya/Wanwan, item magic ke Zhuxin/Kadita. Tidak ada single carry — damage tersebar "
         "fisik + magic sehingga tidak ada satu counter keras.",
         unverified=True, custom_brew=True,
         notes="Racikan Jewel: fondasi anti-counter (jack-of-all-trades). Kuat lawan semua, tidak seledak "
               "comp 6-piece fokus. Belum teruji di rank, coba di casual dulu."),
]

# ---------------- WRITE ----------------
def main():
    commanders_doc = {
        "patch": PATCH,
        "updated": "2026-09-29",
        "count": len(COMMANDERS),
        "commanders": COMMANDERS,
    }
    equipment_doc = {
        "patch": PATCH,
        "updated": "2026-09-29",
        "count": len(EQUIPMENT),
        "equipment": EQUIPMENT,
    }
    comps_doc = {
        "patch": PATCH,
        "updated": "2026-09-29",
        "count": len(COMPS),
        "mechanics": MECHANICS,
        "comps": COMPS,
    }
    for name, doc in (("commanders.json", commanders_doc),
                      ("equipment.json", equipment_doc),
                      ("meta_comps.json", comps_doc)):
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("wrote", path)
    # duplicate-id sanity check
    for label, items in (("commanders", COMMANDERS), ("equipment", EQUIPMENT),
                         ("comps", COMPS)):
        ids = [i["id"] for i in items]
        assert len(ids) == len(set(ids)), f"duplicate ids in {label}: {ids}"
    print("counts:", len(COMMANDERS), len(EQUIPMENT), len(COMPS))

if __name__ == "__main__":
    main()
