import type { CSSProperties } from "react"
import { WordmarkFooter } from "./wordmark-footer"

// UNTLD Mumbai Luxury Streetwear Design Tokens
const untldSettings = {
  name: "UNTLD",
  legalName: "UNTLD MUMBAI",
  background: "#FFFFFF",
  card: "#F4F4F4",
  text: "#000000",
  muted: "#6D6D6D",
  primary: "#121212",
}

function untldTheme(s: typeof untldSettings) {
  const tokens: Record<string, string> = {
    background: s.background,
    foreground: s.text,
    card: s.card,
    primary: s.primary,
    "muted-foreground": s.muted,
  }
  return Object.fromEntries(
    Object.entries(tokens).flatMap(([k, v]) => [[`--${k}`, v], [`--color-${k}`, v]])
  ) as CSSProperties
}

export default function UNTLDFooterDemo() {
  const s = untldSettings
  const fontDisplay = "'Unbounded', 'Switzer', -apple-system, sans-serif"

  return (
    <div
      className="flex min-h-svh w-full flex-col justify-end"
      style={{
        ...untldTheme(s),
        "--font-display": fontDisplay,
        fontFamily: fontDisplay,
        background: s.background,
      } as CSSProperties}
    >
      <WordmarkFooter
        name="UNTLD"
        legalName="UNTLD MUMBAI"
        year={2026}
        description="Raw Japanese selvedge denim and architectural silhouettes engineered for modern urban life. Operating out of Bandra West, Mumbai."
        status="Atelier open // Pali Hill, Bandra West"
        email="vault@untld.in"
        credit={{ label: "19.0596° N, 72.8295° E", href: "#atelier" }}
        columns={[
          {
            title: "Collections",
            links: [
              { label: "The Denim Vault", href: "#vault" },
              { label: "Fall 2026 Core", href: "#vault" },
              { label: "Raw Selvedge Archive", href: "#vault" },
              { label: "Double Knee Series", href: "#vault" },
            ],
          },
          {
            title: "Flagship Atelier",
            links: [
              { label: "Bandra West Space", href: "#atelier" },
              { label: "Archive Appointments", href: "#atelier" },
              { label: "Union Special Alterations", href: "#atelier" },
              { label: "Stockists & Stores", href: "#atelier" },
            ],
          },
          {
            title: "Client Care",
            links: [
              { label: "Complimentary Shipping", href: "#vault" },
              { label: "Sizing & Fit Matrix", href: "#vault" },
              { label: "Terms & Conditions", href: "#" },
              { label: "Privacy Protocol", href: "#" },
            ],
          },
        ]}
      />
    </div>
  )
}
