const RATES: Record<string, number> = { USD: 1, EUR: 0.92, GBP: 0.79, INR: 83.4, JPY: 149.8 }

export default {
  description: "Convert an amount between currencies at Acme's fixed planning rates (USD, EUR, GBP, INR, JPY).",
  args: {
    amount: { type: "number", description: "The amount to convert." },
    from: { type: "string", description: "ISO code of the currency the amount is in." },
    to: { type: "string", description: "ISO code of the currency to convert to." },
  },
  async execute(args: { amount: number; from: string; to: string }) {
    const from = RATES[args.from?.toUpperCase()]
    const to = RATES[args.to?.toUpperCase()]
    if (from === undefined || to === undefined) {
      throw new Error(`fx_rate knows only ${Object.keys(RATES).join(", ")}`)
    }
    const converted = (args.amount / from) * to
    return JSON.stringify({ amount: Math.round(converted * 100) / 100, currency: args.to.toUpperCase(), source: "fx_rate" })
  },
}
