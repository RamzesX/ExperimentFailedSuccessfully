# River Water Filtration System - Complete Technical Specification

**Purpose:** Treating river water for drinking purposes  
**Capacity:** 50 liters/day  
**Service life:** 5 years  
**Number of users:** 5 persons  
**Redundancy:** 2 complete sets  

---

## 1. System Operating Principle

The system utilizes multi-stage gravity filtration. River water flows through successive layers of filter media, each removing a specific type of contaminant. The conical nested bucket design eliminates the need for seals and fasteners — sealing is ensured by the weight of the media and cone geometry.

**NOTE:** This system does NOT provide full bacteriological protection without final boiling. Unlike SafeSand/BioSand-type systems, where slow filtration (0.1-0.4 m/h) allows for biofilm formation (schmutzdecke) that biologically breaks down pathogens, filtration here is significantly faster (~2-4 m/h). Therefore, the final mechanical barrier is the 0.5μm sintered filter, and ultimate sterilization is provided by boiling.

---

## 2. Filter Layers - Description and Rationale

### Layer 1: Gravel (Pre-filter)

| Parameter | Value |
|-----------|-------|
| Thickness | 8 cm |
| Fraction | 8-16 mm |
| Material | River gravel, washed |
| Quantity per set | 7.5 kg |
| Screen underneath | 5 mm mesh |

**Function:** Retains large contaminants — leaves, twigs, larger organic particles, coarse sand. Protects subsequent layers from rapid clogging. Easy to rinse and regenerate.

**Regeneration:** Rinse with water every 1-2 weeks. Practically unlimited lifespan.

---

### Layer 2: Quartz Sand (Mechanical Filter)

| Parameter | Value |
|-----------|-------|
| Thickness | 18 cm |
| Fraction | 0.5-1.5 mm |
| Material | Quartz filter sand (SiO₂ >95%) |
| Quantity per set | 12.5 kg |
| Screen underneath | 0.3 mm mesh (60 mesh) |

**Function:** Mechanical filtration of fine suspensions, silt, colloidal clay. Angular grains (not rounded) create better filter structure.

**Mineral specification:**
- Quartz (SiO₂) minimum 95%
- No carbonite (CaCO₃ <1%)
- Angular grains, not rounded
- Color: white, gray, or slightly yellowish (yellow = iron oxides, acceptable)

**Where to buy:** Pool/filter sand, certified playground sand, aquarium supply stores.

**Regeneration:** Rinse every 2-4 weeks. Calcining in oven (200°C, 2h) once yearly eliminates any microorganisms. Lifespan 10+ years.

---

### Layer 3: Iron Filings Fe⁰ (Chemical Reduction)

| Parameter | Value |
|-----------|-------|
| Thickness | 12 cm |
| Fraction | 1-3 mm |
| Material | Pure metallic iron (Fe⁰), NOT steel |
| Quantity per set | 7.5 kg |
| Screen underneath | 0.5 mm mesh (35 mesh) |

**Chemical function:**

1. **Nitrate reduction (NO₃⁻) to ammonia (NH₄⁺):**
   ```
   NO₃⁻ + 4Fe⁰ + 10H⁺ → NH₄⁺ + 4Fe²⁺ + 3H₂O
   ```
   Ammonia is subsequently captured by zeolite in the next layer.

2. **Arsenic removal (As):**
   Fe⁰ reduces As(V) to As(III), which co-precipitates with iron hydroxides.

3. **Heavy metal removal:**
   Pb, Cu, Cd, Cr(VI) — reduction and sorption on iron surface and corrosion products.

4. **Halogenated compound degradation:**
   Pesticides, chlorinated solvents — reductive dechlorination.

**NOTE:** Must be pure iron (Fe⁰), not stainless steel. Stainless steel contains chromium and nickel which can leach. Best source: filings from lathe/milling machine working pure iron, steel wool (but check composition — must be >99% Fe).

**Regeneration:** Replacement every 2-3 years (iron is consumed in reactions). Spent filings can be composted.

---

### Layer 4: Zeolite (Ion Exchange)

| Parameter | Value |
|-----------|-------|
| Thickness | 15 cm |
| Fraction | 2-4 mm |
| Material | Natural clinoptilolite |
| Quantity per set | 12.5 kg |
| Screen underneath | 1.5 mm mesh (12 mesh) |

**Function:**

1. **Ammonia sorption (NH₄⁺):**
   Captures ammonia produced from nitrate reduction in the iron layer.
   ```
   Zeolite-Na⁺ + NH₄⁺ → Zeolite-NH₄⁺ + Na⁺
   ```

2. **Heavy metal ion exchange:**
   Pb²⁺, Cd²⁺, Cu²⁺, Zn²⁺ — selective sorption.

3. **Radioactive element sorption:**
   - Cesium-137 (Cs⁺) — very high selectivity
   - Strontium-90 (Sr²⁺) — good sorption
   - Radium-226 (Ra²⁺)
   
   Clinoptilolite was used at Chernobyl and Fukushima for water decontamination.

4. **Water softening:**
   Exchange of Ca²⁺ and Mg²⁺ for Na⁺.

**Regeneration:** Soaking in 10% NaCl solution (table salt) for 24h, then rinsing. Allows for 20-50 regeneration cycles. Lifespan 5-10 years with regular regeneration.

---

### Layer 5: Activated Carbon (Adsorption)

| Parameter | Value |
|-----------|-------|
| Thickness | 25 cm |
| Fraction | 1-3 mm (granular) |
| Material | Coconut carbon, iodine number >900 mg/g |
| Quantity per set | 30 kg |
| Screen underneath | 0.8 mm mesh (20 mesh) |

**Function:**

1. **Organic compound adsorption:**
   - Pesticides, herbicides
   - Humic substances (color, odor)
   - Hydrocarbons, oils
   - Phenols, detergents

2. **Chlorine and chloramine removal:**
   Catalytic reduction.

3. **Taste and odor improvement:**
   Elimination of volatile organic compounds.

4. **Some heavy metal adsorption:**
   Mercury, lead — supplementary.

**Coconut distillery carbon specification:**
- Iodine number: >900 mg/g (higher = better adsorption)
- Ash content: <3%
- Hardness: >95% (less dusting)
- Granulation: 8x30 mesh (0.6-2.4 mm)

**Partial regeneration:** Calcining in oven without air access (in sealed container) at 300-400°C for 2h restores some capacity. Full regeneration requires 800-900°C and specialized equipment. Practical approach: replacement every 2-3 years or when water develops smell/taste.

---

### Layer 6: Sintered Metal Filter 0.5μm (Microbiological Barrier)

| Parameter | Value |
|-----------|-------|
| Material | 316L sintered stainless steel |
| Porosity | 0.5 μm |
| Form | Ø260mm disc or tube |
| Quantity per set | 1 pc. |

**Function:**

1. **Bacterial barrier:**
   Most pathogenic bacteria are 0.5-5 μm in size:
   - E. coli: 1-2 μm
   - Salmonella: 0.7-1.5 μm
   - Cholera (Vibrio): 1-3 μm
   
   The 0.5μm sintered filter retains >99% of bacteria.

2. **Protozoan barrier:**
   - Giardia: 8-15 μm (cysts)
   - Cryptosporidium: 4-6 μm (oocysts)
   
   100% retention.

3. **Fine suspension barrier:**
   Everything that passed through previous layers.

**NOTE:** Viruses (0.02-0.3 μm) PASS THROUGH the sintered filter. That's why boiling is essential!

**Regeneration:** 
- Backwash weekly (reverse flow with clean water)
- Ultrasonic cleaning monthly
- Boiling in water every 3 months (sterilization)
- Lifespan: practically unlimited

---

### Layer 7: Boiling (Final Sterilization)

| Parameter | Value |
|-----------|-------|
| Temperature | 100°C (boiling point) |
| Time | Minimum 1 minute of rolling boil |
| At altitude >2000m | Minimum 3 minutes |

**Function:**

Elimination of viruses and spore forms:
- Hepatitis A viruses, rotaviruses, noroviruses
- Bacterial spores (Clostridium)
- Amoebae and their cysts

**This is the final and crucial step!** Even the best mechanical filter cannot replace boiling.

---

## 3. Conical Bucket Construction

### Nesting Principle

Buckets have a truncated cone shape. The narrower part (bottom) fits into the wider part (top) of the next bucket. Sealing is ensured by:
- Cone geometry
- Weight of filter media
- No need for gaskets

### Standard Dimensions

```
        ┌─────────── Ø 300 mm ───────────┐
        │                                 │
        \                                 /
         \                               /
          \                             /
           \                           /
            \                         /
             \                       /
              └───── Ø 260 mm ──────┘

Total height: 250 mm
Working height (media): 180-200 mm
Water space above media: 50-70 mm
Wall angle: ~4.5°
```

### Sheet Metal Pattern (for one bucket)

To cut from stainless steel sheet, a ring sector is needed:

```
Outer radius (R₁): 1450 mm
Inner radius (R₂): 1260 mm
Sector angle (α): 65°

Sheet area per bucket: ~0.22 m²
```

**Truncated cone development formula:**
```
R₁ = H × r₁ / (r₁ - r₂)
R₂ = H × r₂ / (r₁ - r₂)
α = 360° × r₁ / R₁

where:
H = cone height = 250 mm
r₁ = upper radius = 150 mm
r₂ = lower radius = 130 mm
```

### Bucket Assembly

1. Cut sector from sheet according to template
2. Roll into cone, edges overlapping 10mm
3. Single longitudinal weld
4. Weld stainless screen to bottom edge
5. Optional: flare upper edge outward (stiffening flange)

### Dimension Table for Each Layer

| Layer | Media thickness | Bucket height | Screen mesh | Screen wire |
|-------|-----------------|---------------|-------------|-------------|
| 1. Gravel | 80 mm | 150 mm | 5.0 mm | 1.0 mm |
| 2. Sand | 180 mm | 250 mm | 0.3 mm | 0.2 mm |
| 3. Fe⁰ | 120 mm | 180 mm | 0.5 mm | 0.25 mm |
| 4. Zeolite | 150 mm | 220 mm | 1.5 mm | 0.5 mm |
| 5. Carbon | 250 mm | 320 mm | 0.8 mm | 0.3 mm |
| 6. Sintered | - | 100 mm | (sintered instead of screen) | - |
| 7. Tank | - | 400 mm | (no screen, with tap) | - |

**Total stack height:** ~1620 mm (~1.6 m)

---

## 4. Materials Specification

### Stainless Steel Sheet

| Parameter | Value |
|-----------|-------|
| Grade | 304 (1.4301) or 316L (1.4404) |
| Thickness | 1.0-1.5 mm |
| Quantity for 2 sets | ~4 m² |
| Finish | 2B (matte) or BA |

**Note:** 304 steel is sufficient for freshwater. 316L only if water has elevated chloride content (>250 mg/L) or salinity.

### Woven Stainless Screen

| Mesh | Trade name | Quantity for 2 sets |
|------|------------|---------------------|
| 5.0 mm | Woven screen 5x5 | 0.3 m² |
| 1.5 mm | 12 mesh screen | 0.3 m² |
| 0.8 mm | 20 mesh screen | 0.3 m² |
| 0.5 mm | 35 mesh screen | 0.3 m² |
| 0.3 mm | 60 mesh screen | 0.3 m² |

**Screen material:** 304 or 316 steel. Buy ready-made woven cloth, don't make by hand from wire (uneven mesh, waste of time).

### Sintered Metal

| Parameter | Value |
|-----------|-------|
| Material | 316L |
| Porosity | 0.5 μm |
| Form | Ø260mm disc or Ø50x200mm tube |
| Thickness | 2-3 mm |
| Quantity | 2 pcs. (one per set) |

**Where to buy:** Aliexpress, eBay — search "sintered stainless steel filter 0.5 micron 316L"

---

## 5. Welding

### Welder

| Parameter | Recommended minimum | Optimal |
|-----------|---------------------|---------|
| Type | MIG/MAG | TIG (GTAW) |
| Current | 130A | 160-200A |
| Gas | Ar/CO₂ mix (82/18) | Pure argon (99.99%) |

**TIG is best for stainless**, but MIG will work with proper settings.

**If you don't have a welder:** commissioning welding from a metalworker costs ~$15-25 for the entire bucket set.

### Welding Materials

| Material | Specification | Quantity for 2 sets |
|----------|---------------|---------------------|
| Wire/electrode | ER308L (for 304) or ER316L (for 316L) | 0.5 kg |
| Shielding gas | Argon 4.6 or higher | 1 × 8L cylinder |

### Welding Parameters

| Parameter | Value for 1.0-1.5mm sheet |
|-----------|---------------------------|
| Current | 50-80A (TIG) / 80-100A (MIG) |
| Voltage | 10-12V (TIG) / 18-20V (MIG) |
| Speed | 10-15 cm/min |
| Gas flow | 8-10 L/min |

### Tips

1. **Preparation:** Clean edges of grease (acetone/alcohol)
2. **Position:** Weld in flat position (PA) if possible
3. **Sequence:** First tack weld every 30-50mm, then continuous weld
4. **Cooling:** Don't quench in water — cool slowly
5. **Inspection:** Weld must be continuous, no gaps or porosity

---

## 6. Cost Estimate (2 complete sets for 5 years)

### Filter Media

| Material | Quantity | Unit price | Cost |
|----------|----------|------------|------|
| River gravel | 15 kg | $0.50/kg | $7.50 |
| Quartz filter sand | 25 kg | $0.75/kg | $18.75 |
| Iron filings Fe⁰ | 30 kg* | $2.50/kg | $75 |
| Zeolite clinoptilolite | 25 kg | $2/kg | $50 |
| Coconut activated carbon | 60 kg | $6.25/kg | $375 |
| **Total media** | | | **$526** |

*Iron filings: 15 kg × 2 replacements over 5 years

### Construction Materials

| Material | Quantity | Unit price | Cost |
|----------|----------|------------|------|
| Stainless sheet 304 1.5mm | 4 m² | $37.50/m² | $150 |
| Stainless screen (set) | 2 m² | $25/m² | $50 |
| Sintered 316L 0.5μm | 2 pcs. | $37.50/pc. | $75 |
| Stainless tap | 2 pcs. | $7.50/pc. | $15 |
| **Total construction** | | | **$290** |

### Welding and Tools

| Item | Cost |
|------|------|
| ER308L welding wire 0.5kg | $12.50 |
| Argon gas (service/cylinder) | $25 |
| Welding commission (option) | $37.50 |
| **Total welding** | **$37-75** |

### Cost Summary

| Category | Cost |
|----------|------|
| Filter media (5 years) | $526 |
| Construction materials | $290 |
| Welding | ~$50 |
| Salt for zeolite regeneration (5 years) | $12.50 |
| 10% reserve | ~$88 |
| **TOTAL** | **~$966** |

**Cost per person:** ~$193 / 5 years = ~$39/year = ~$3.25/month

**Cost per liter of water:** $966 / 91,250 L = **$0.011/L** (about 1 cent per liter)

---

## 7. Maintenance Schedule

### Daily
- Check water flow
- Boil filtered water before consumption

### Weekly
- Backwash sintered filter (reverse and flush with clean water)
- Visual inspection of layers

### Every 2-4 weeks
- Rinse gravel and sand
- Check water level above layers

### Every 3 months
- Boil sintered filter (sterilization)
- Check condition of iron filings (color, volume)

### Yearly
- Calcine sand (200°C, 2h)
- Regenerate zeolite (10% NaCl, 24h soak)
- Assess activated carbon condition

### Every 2-3 years
- Replace iron filings
- Replace or reactivate activated carbon

---

## 8. Depletion and Replacement Indicators

| Layer | Depletion symptom | Action |
|-------|-------------------|--------|
| Gravel | Heavy soiling, odor | Rinse or replace |
| Sand | Slow flow despite rinsing | Calcine or replace |
| Fe⁰ | Color change to rusty, volume decrease >30% | Replace |
| Zeolite | No effect after salt regeneration | Replace |
| Carbon | Taste/odor in water despite boiling | Replace |
| Sintered | Slow flow despite backwash | Ultrasonic cleaning |

---

## 9. Material Sources

### Filter Media
- **Filter sand:** Pool supply stores, Amazon/eBay ("pool filter sand")
- **Zeolite:** Aquarium stores, agricultural supply (feed additive), Amazon
- **Activated carbon:** Distillery supply, Amazon ("coconut activated carbon granular")
- **Iron filings:** Machine shops/metal workshops, Amazon/eBay ("steel wool", "iron filings")

### Construction Materials
- **Stainless sheet:** Metal suppliers, industrial supply, eBay
- **Stainless screen:** Screening/mesh suppliers, Amazon ("stainless woven mesh")
- **Sintered 316L:** Aliexpress, eBay ("sintered stainless steel filter 0.5 micron")

### Welding
- **ER308L/ER316L wire:** Welding supply stores, Amazon
- **Argon:** Welding gas suppliers, industrial gas distributors

---

## 10. Safety and Warnings

1. **Always boil water before consumption** — mechanical filtration does not eliminate viruses

2. **Do not use steel other than stainless** — corrosion = heavy metals in water

3. **Filings must be pure iron** — stainless steel releases chromium and nickel

4. **Test water periodically** if you have access to testing (E.coli, nitrates)

5. **Do not use water from industrial rivers** — system does not remove all industrial chemicals

6. **Regularly regenerate zeolite** — saturated zeolite may release contaminants

7. **When welding:** safety glasses, gloves, ventilation (stainless fumes are toxic)

---

## 11. Appendices

### A. Sheet Metal Cutting Template

```
     CONICAL BUCKET TEMPLATE (scale 1:10)
     
              Roll axis
                  ↓
     ┌────────────┬────────────┐
     │            │            │
     │     ╭──────┴──────╮     │
     │    ╱               ╲    │
     │   ╱                 ╲   │
     │  ╱                   ╲  │
     │ ╱                     ╲ │
     │╱                       ╲│
     ╱           65°           ╲
    ╱                           ╲
   ╱──────────────┬──────────────╲
  ╱               │               ╲
 ╱                │                ╲
╱     R₂=1260mm   │   R₁=1450mm    ╲
─────────────────────────────────────
     
     Weld overlap: +10mm on both sides of arc
```

### B. System Assembly Diagram

```
          [River water inlet]
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 1 - GRAVEL       ║ H=150mm
    ║   ○○○○○○○○○○○○○○○○○○○○○   ║
    ╠═══════════════════════════╣ 5mm screen
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 2 - SAND         ║ H=250mm
    ║   ::::::::::::::::::::::: ║
    ╠═══════════════════════════╣ 0.3mm screen
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 3 - Fe⁰          ║ H=180mm
    ║   ·························║
    ╠═══════════════════════════╣ 0.5mm screen
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 4 - ZEOLITE      ║ H=220mm
    ║   ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○   ║
    ╠═══════════════════════════╣ 1.5mm screen
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 5 - CARBON       ║ H=320mm
    ║   ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪  ║
    ╠═══════════════════════════╣ 0.8mm screen
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 6 - SINTERED     ║ H=100mm
    ║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ║ 0.5μm
    ╠═══════════════════════════╣
                  │
                  ▼
    ╔═══════════════════════════╗
    ║   BUCKET 7 - TANK         ║ H=400mm
    ║                           ║
    ║         [TAP] ═══════►    ║
    ╚═══════════════════════════╝
                  │
                  ▼
            [BOILING]
                  │
                  ▼
          [DRINKING WATER]
```

---

**Document prepared: January 2026**  
**Version: 1.0**
