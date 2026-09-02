"use client";

import {
  ArrowUpRight,
  BarChart3,
  Brain,
  DollarSign,
  TrendingUp,
  Zap,
} from "lucide-react";

const forecastData = [
  { day: "Mar 26", actual: 2.1, predicted: 2.4 },
  { day: "Mar 27", actual: 1.8, predicted: 2.0 },
  { day: "Mar 28", actual: 2.7, predicted: 2.5 },
  { day: "Mar 29", actual: 2.2, predicted: 2.4 },
  { day: "Mar 30", actual: 3.1, predicted: 2.8 },
  { day: "Mar 31", actual: 2.6, predicted: 2.9 },
  { day: "Apr 01", actual: 3.4, predicted: 3.1 },
];

const features = [
  ["Rolling demand · 28d", 1568],
  ["Rolling demand · 7d", 1358],
  ["Demand volatility · 7d", 918],
  ["Previous day demand", 847],
  ["Previous week demand", 829],
  ["Previous 28d demand", 741],
];

const pricing = [
  { change: "-10%", price: "$0.63", demand: "3.18", revenue: "$2.00" },
  { change: "-5%", price: "$0.67", demand: "2.97", revenue: "$1.97" },
  { change: "0%", price: "$0.70", demand: "2.76", revenue: "$1.93" },
  { change: "+5%", price: "$0.74", demand: "2.55", revenue: "$1.88" },
  { change: "+10%", price: "$0.77", demand: "2.35", revenue: "$1.81" },
];

export default function Home() {
  return (
    <main className="min-h-screen bg-[#08090b] text-white">
      {/* NAVBAR */}
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6 lg:px-8">
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-white text-black">
            <TrendingUp size={19} />
          </div>
          <span className="text-lg font-semibold tracking-tight">
            DemandLens
          </span>
        </div>

        <div className="hidden items-center gap-8 text-sm text-zinc-400 md:flex">
          <a href="#forecast" className="transition hover:text-white">
            Forecast
          </a>
          <a href="#pricing" className="transition hover:text-white">
            Pricing
          </a>
          <a href="#methodology" className="transition hover:text-white">
            Methodology
          </a>
        </div>

        <div className="rounded-full border border-zinc-800 px-4 py-2 text-xs text-zinc-400">
          ML-powered retail intelligence
        </div>
      </nav>

      {/* HERO */}
      <section className="mx-auto max-w-7xl px-6 pb-20 pt-16 lg:px-8 lg:pt-24">
        <div className="max-w-4xl">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-zinc-800 bg-zinc-900/60 px-3 py-1.5 text-xs text-zinc-400">
            <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
            Demand forecasting + pricing intelligence
          </div>

          <h1 className="text-5xl font-semibold tracking-[-0.04em] sm:text-6xl lg:text-7xl">
            Turn retail data into
            <span className="block text-zinc-400">
              smarter decisions.
            </span>
          </h1>

          <p className="mt-7 max-w-2xl text-lg leading-8 text-zinc-400">
            DemandLens uses machine learning to forecast product demand,
            understand demand patterns, and evaluate pricing scenarios for
            potential revenue impact.
          </p>

          <div className="mt-9 flex flex-wrap gap-3">
            <a
              href="#forecast"
              className="flex items-center gap-2 rounded-lg bg-white px-5 py-3 text-sm font-medium text-black transition hover:bg-zinc-200"
            >
              Explore the model
              <ArrowUpRight size={16} />
            </a>

            <a
              href="#methodology"
              className="rounded-lg border border-zinc-800 px-5 py-3 text-sm text-zinc-300 transition hover:border-zinc-600"
            >
              How it works
            </a>
          </div>
        </div>
      </section>

      {/* KPI STRIP */}
      <section className="border-y border-zinc-900 bg-[#0b0c0f]">
        <div className="mx-auto grid max-w-7xl grid-cols-2 lg:grid-cols-4">
          <Metric label="Forecast MAE" value="1.069" />
          <Metric label="Forecast RMSE" value="2.235" />
          <Metric label="MAE improvement" value="19.95%" />
          <Metric label="Forecasting model" value="LightGBM" />
        </div>
      </section>

      {/* FORECAST */}
      <section
        id="forecast"
        className="mx-auto max-w-7xl scroll-mt-10 px-6 py-24 lg:px-8"
      >
        <SectionHeader
          number="01"
          title="Demand Forecasting"
          description="Predict near-term product demand using historical sales, seasonality, price signals and engineered demand features."
        />

        <div className="mt-10 grid gap-6 lg:grid-cols-[1fr_300px]">
          <div className="rounded-2xl border border-zinc-800 bg-[#0d0f12] p-6">
            <div className="mb-8 flex items-center justify-between">
              <div>
                <p className="text-sm font-medium">Actual vs predicted demand</p>
                <p className="mt-1 text-xs text-zinc-500">
                  Example product · CA_1 / HOBBIES_1_001
                </p>
              </div>

              <div className="flex gap-4 text-xs text-zinc-500">
                <span>● Actual</span>
                <span>● Predicted</span>
              </div>
            </div>

            <div className="flex h-72 items-end gap-3 border-b border-zinc-800 px-2 pb-0">
              {forecastData.map((item, index) => {
                const actualHeight = `${(item.actual / 4) * 100}%`;
                const predictedHeight = `${(item.predicted / 4) * 100}%`;

                return (
                  <div
                    key={item.day}
                    className="flex h-full flex-1 items-end justify-center gap-1"
                  >
                    <div className="relative flex h-full w-1/3 items-end">
                      <div
                        className="w-full rounded-t bg-zinc-500 transition hover:bg-zinc-300"
                        style={{ height: actualHeight }}
                      />
                    </div>

                    <div className="relative flex h-full w-1/3 items-end">
                      <div
                        className="w-full rounded-t bg-white transition hover:bg-zinc-300"
                        style={{ height: predictedHeight }}
                      />
                    </div>

                    <span className="absolute mt-[305px] text-[10px] text-zinc-600">
                      {item.day}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          <div className="space-y-4">
            <InfoCard
              icon={<Brain size={18} />}
              title="LightGBM"
              text="Gradient-boosted decision trees trained on product-store demand patterns."
            />

            <InfoCard
              icon={<BarChart3 size={18} />}
              title="Time-aware features"
              text="1, 7 and 28-day lags plus rolling demand statistics capture recent behavior."
            />

            <InfoCard
              icon={<Zap size={18} />}
              title="19.95% improvement"
              text="Lower MAE compared with the simple 7-day demand baseline."
            />
          </div>
        </div>
      </section>

      {/* FEATURE IMPORTANCE */}
      <section className="border-y border-zinc-900 bg-[#0b0c0f]">
        <div className="mx-auto max-w-7xl px-6 py-24 lg:px-8">
          <SectionHeader
            number="02"
            title="What drives the forecast?"
            description="The model relies heavily on recent demand history and rolling demand behavior."
          />

          <div className="mt-10 grid gap-3">
            {features.map(([name, value], index) => {
              const width = `${(Number(value) / 1568) * 100}%`;

              return (
                <div
                  key={name}
                  className="grid grid-cols-[35px_1fr_70px] items-center gap-4 rounded-xl border border-zinc-900 bg-[#0d0f12] p-4"
                >
                  <span className="text-xs text-zinc-600">
                    0{index + 1}
                  </span>

                  <div>
                    <div className="mb-2 flex justify-between text-sm">
                      <span className="text-zinc-300">{name}</span>
                      <span className="text-zinc-500">
                        {Number(value).toLocaleString()}
                      </span>
                    </div>

                    <div className="h-1.5 overflow-hidden rounded-full bg-zinc-800">
                      <div
                        className="h-full rounded-full bg-zinc-300"
                        style={{ width }}
                      />
                    </div>
                  </div>

                  <span className="text-right text-xs text-zinc-600">
                    signal
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* PRICING */}
      <section
        id="pricing"
        className="mx-auto max-w-7xl scroll-mt-10 px-6 py-24 lg:px-8"
      >
        <SectionHeader
          number="03"
          title="Pricing Intelligence"
          description="Evaluate how different price points could affect expected demand and revenue under multiple elasticity assumptions."
        />

        <div className="mt-10 grid gap-6 lg:grid-cols-[1fr_340px]">
          <div className="overflow-hidden rounded-2xl border border-zinc-800 bg-[#0d0f12]">
            <div className="border-b border-zinc-800 p-6">
              <p className="text-sm font-medium">
                Price scenario analysis
              </p>
              <p className="mt-1 text-xs text-zinc-500">
                Example: WI_3 / HOBBIES_1_030 · current price $0.70
              </p>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead className="border-b border-zinc-800 text-xs text-zinc-500">
                  <tr>
                    <th className="px-6 py-4 font-medium">Price change</th>
                    <th className="px-6 py-4 font-medium">Price</th>
                    <th className="px-6 py-4 font-medium">Demand</th>
                    <th className="px-6 py-4 font-medium">Revenue</th>
                  </tr>
                </thead>

                <tbody>
                  {pricing.map((row) => (
                    <tr
                      key={row.change}
                      className="border-b border-zinc-900 last:border-0"
                    >
                      <td className="px-6 py-4 text-zinc-300">
                        {row.change}
                      </td>
                      <td className="px-6 py-4">{row.price}</td>
                      <td className="px-6 py-4 text-zinc-400">
                        {row.demand}
                      </td>
                      <td className="px-6 py-4 font-medium">
                        {row.revenue}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="rounded-2xl border border-zinc-800 bg-[#0d0f12] p-7">
            <div className="mb-5 flex h-10 w-10 items-center justify-center rounded-lg bg-white text-black">
              <DollarSign size={19} />
            </div>

            <p className="text-sm text-zinc-500">Illustrative recommendation</p>

            <h3 className="mt-2 text-3xl font-semibold tracking-tight">
              $0.77
            </h3>

            <p className="mt-2 text-sm leading-6 text-zinc-500">
              Under the -0.5 elasticity assumption, the +10% price scenario
              produces the highest estimated revenue in this example.
            </p>

            <div className="mt-7 border-t border-zinc-800 pt-5">
              <div className="flex justify-between text-sm">
                <span className="text-zinc-500">Estimated revenue</span>
                <span>$2.02</span>
              </div>

              <div className="mt-3 flex justify-between text-sm">
                <span className="text-zinc-500">Estimated demand</span>
                <span>2.62 units</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* METHODOLOGY */}
      <section
        id="methodology"
        className="border-t border-zinc-900 bg-[#0b0c0f]"
      >
        <div className="mx-auto max-w-7xl px-6 py-24 lg:px-8">
          <SectionHeader
            number="04"
            title="How DemandLens works"
            description="A complete pipeline from historical retail data to forecasting and pricing scenarios."
          />

          <div className="mt-12 grid gap-3 md:grid-cols-5">
            <PipelineStep number="01" title="Sales Data" text="Historical product-store sales" />
            <PipelineStep number="02" title="Features" text="Lags, rolling statistics & price signals" />
            <PipelineStep number="03" title="LightGBM" text="Machine-learning demand forecast" />
            <PipelineStep number="04" title="Elasticity" text="Price-demand scenarios" />
            <PipelineStep number="05" title="Decision" text="Revenue-aware pricing insight" />
          </div>

          <div className="mt-16 border-t border-zinc-800 pt-8">
            <p className="mb-5 text-xs uppercase tracking-[0.2em] text-zinc-600">
              Technology
            </p>

            <div className="flex flex-wrap gap-2">
              {[
                "Python",
                "Pandas",
                "scikit-learn",
                "LightGBM",
                "Next.js",
                "TypeScript",
                "Tailwind CSS",
                "Recharts",
                "Vercel",
              ].map((tech) => (
                <span
                  key={tech}
                  className="rounded-full border border-zinc-800 px-4 py-2 text-xs text-zinc-400"
                >
                  {tech}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="mx-auto flex max-w-7xl flex-col gap-3 px-6 py-10 text-xs text-zinc-600 sm:flex-row sm:items-center sm:justify-between lg:px-8">
        <span>DemandLens · Retail demand intelligence</span>
        <span>Forecasting · Analytics · Pricing Optimization</span>
      </footer>
    </main>
  );
}


/* -------------------------------------------------------
   Components
------------------------------------------------------- */

function Metric({
  label,
  value,
}: {
  label: string;
  value: string;
}) {
  return (
    <div className="border-r border-zinc-900 px-6 py-7 last:border-r-0 lg:px-8">
      <p className="text-xs text-zinc-600">{label}</p>
      <p className="mt-2 text-2xl font-semibold tracking-tight">
        {value}
      </p>
    </div>
  );
}


function SectionHeader({
  number,
  title,
  description,
}: {
  number: string;
  title: string;
  description: string;
}) {
  return (
    <div className="max-w-2xl">
      <p className="text-xs font-medium tracking-[0.2em] text-zinc-600">
        {number}
      </p>

      <h2 className="mt-3 text-3xl font-semibold tracking-[-0.03em] sm:text-4xl">
        {title}
      </h2>

      <p className="mt-4 leading-7 text-zinc-500">
        {description}
      </p>
    </div>
  );
}


function InfoCard({
  icon,
  title,
  text,
}: {
  icon: React.ReactNode;
  title: string;
  text: string;
}) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-[#0d0f12] p-5">
      <div className="mb-4 flex h-9 w-9 items-center justify-center rounded-lg border border-zinc-800 text-zinc-300">
        {icon}
      </div>

      <p className="text-sm font-medium">{title}</p>

      <p className="mt-2 text-xs leading-5 text-zinc-500">
        {text}
      </p>
    </div>
  );
}


function PipelineStep({
  number,
  title,
  text,
}: {
  number: string;
  title: string;
  text: string;
}) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-[#0d0f12] p-5">
      <span className="text-xs text-zinc-600">{number}</span>

      <h3 className="mt-8 text-sm font-medium">{title}</h3>

      <p className="mt-2 text-xs leading-5 text-zinc-500">
        {text}
      </p>
    </div>
  );
}

