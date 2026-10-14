# Image derived palette

The user supplied `image(20261014-201305).png` as a color reference. A 16-color adaptive quantization of a resized RGB image yielded these exact representative colors:

| Role | Color | Use |
| --- | --- | --- |
| Space | #070b15 | Page background and code background |
| Deep blue | #0b2646 | Header, outline and lesson surface |
| Pale light | #e0dcf8 | Primary text |
| Pale lilac | #bbbcef | Links, buttons and secondary text |
| Ice blue | #6286d3 | Visible borders and focus indicator |
| Mid lilac | #9899d9 | Needs-review chart segment |

Use solid colors. No image, gradient, glow or decorative effect is needed to reproduce a palette. Black text is used on the pale primary buttons. Chart segments have text labels and focus descriptions; color is not the only indicator. Disabled controls are visually muted and have disabled semantics.

`tests/course.test.cjs` verifies WCAG relative-luminance contrast: text and link combinations meet at least 4.5:1; essential borders and the focus color against both backgrounds meet at least 3:1. Browser tests additionally check rendered enabled text/background pairs, focus styling, form controls, sidebar state and mobile overflow.

This is validation of the specified colors and tested interface states, not a claim of complete WCAG conformance for every browser or user setting.
