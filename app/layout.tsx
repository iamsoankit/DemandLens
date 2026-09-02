import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "DemandLens — Demand Forecasting & Pricing Intelligence",
  description:
    "Machine learning powered demand forecasting and pricing optimization platform.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
