# SiteSutra spacing and placement audit — 15 October 2026

## Research applied

- [GOV.UK layout guidance](https://design-system.service.gov.uk/styles/layout/): use responsive layouts and readable text measures rather than stretching prose across desktop widths. SiteSutra now uses a common page edge and a 72ch prose measure within it.
- [GOV.UK headings](https://design-system.service.gov.uk/styles/headings/): make heading styling consistent and preserve the semantic hierarchy. We retain existing H1/H2/H3 structure with separate display and reading scales.
- [GOV.UK spacing](https://design-system.service.gov.uk/styles/spacing/): adapt spacing across screen sizes. Section and card spacing now use a small shared scale rather than independent percentage offsets.
- [Carbon spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview): align component padding and grid gaps through related spacing values. Studio cards, buttons and content groups share gutters and repeated intervals.

These principles guide placement; SiteSutra retains its ivory/blue identity and existing routes rather than adopting either system's visual branding.

## Problems corrected

- Page intros and reading sections had independently capped widths; broad sections drifted to different edges at large viewport sizes.
- Heading top margins combined with section padding to create excessive gaps after introductions.
- CTA panels used 7% gutters while ordinary content used 5%; both now share a viewport-aware inset.
- Four-step processes inherited a seven-column layout. Desktop steps now fit their count; tablet steps use a two-column layout and mobile uses a stacked sequence.
- Card text and action placement varied. Actions sit at the end of equal-height card rows, with consistent padding and line heights.
- The tablet header could wrap navigation into a second row. The accessible menu breakpoint is now 1100px in both CSS and JS.
- Footer identity, tagline, links and phone/WhatsApp now use an intentional responsive grid rather than an uneven flex wrap.
- Both concept demos retain distinct layouts, fonts and colours while sharing disciplined content edges, product/action spacing, project copy and form alignment.

## Implementation

`dist/layout.css` is the final studio layout layer. `dist/demo-layout.css` covers concept demos. Both are content-hashed in generated page links. Existing colours, source imagery, metadata and route content remain intact. The footer identity is grouped in the shared template. The menu continues to support keyboard focus, Escape and no-JavaScript navigation.

## Verification

- Both generators rebuilt; 22 page routes and 585 internal references pass.
- Every page tested at 320, 390, 768, 1024, 1440 and 1920 px: 132 layout checks, no page overflow or viewport-clipped headings.
- After visual correction of CTA gutters, 60 further checks across studio pages verified direct text aligns to the shared page edge at 320/1024/1920 px.
- Visually inspected desktop service hierarchy/footer and mobile homepage. Tested tablet menu open/Escape close, native keyboard FAQ expansion and retail demo bag add/reset.
- No calls, WhatsApp messages, bookings or email drafts submitted during testing. Third-party Cal.com layout is controlled by its embed; the surrounding card/gutters are refined here.
- Production remains unchanged until owner approves the preview PR.
