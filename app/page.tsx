"use client";

import { useMemo, useState } from "react";

const scenarios = [
  { elasticity: -0.5, label: "Low sensitivity" },
  { elasticity: -1.0, label: "Moderate sensitivity" },
  { elasticity: -1.5, label: "High sensitivity" },
];

const priceChanges = [-10, -5, 0, 5, 10];

export default function Home() {
  const [currentPrice, setCurrentPrice] = useState(0.7);
  const [baseDemand, setBaseDemand] = useState(2.762);
  const [elasticity, setElasticity] = useState(-1.0);

  const results = useMemo(() => {
    return priceChanges.map((change) => {
      const pct = change / 100;

      const candidatePrice = currentPrice * (1 + pct);

      // Constant-elasticity demand model:
      // Q1 = Q0 * (P1/P0)^elasticity
      const demand =
        baseDemand *
        Math.pow(candidatePrice / currentPrice, elasticity);

      const revenue = candidatePrice * demand;

      return {
        change,
        price: candidatePrice,
        demand,
        revenue,
      };
    });
  }, [currentPrice, baseDemand, elasticity]);

  const best = results.reduce((a, b) =>
    b.revenue > a.revenue ? b : a
  );

  const currentScenario = results.find((x) => x.change === 0)!;

  const revenueChange =
    ((best.revenue - currentScenario.revenue) /
      currentScenario.revenue) *
    100;

  const maxRevenue = Math.max(...results.map((x) => x.revenue));

  return (
    <main className="page">

      {/* NAVBAR */}
      <nav className="navbar">
        <div className="logo">
          Demand<span>Lens</span>
        </div>

        <div className="navLinks">
          <a href="#forecast">Forecasting</a>
          <a href="#pricing">Pricing</a>
          <a href="#methodology">Methodology</a>
        </div>

        <div className="status">
          <span className="statusDot" />
          Live Demo
        </div>
      </nav>

      {/* HERO */}
      <section className="hero">
        <div className="heroText">
          <div className="eyebrow">
            RETAIL DEMAND INTELLIGENCE
          </div>

          <h1>
            Forecast demand.
            <br />
            <span>Optimize price.</span>
          </h1>

          <p>
            DemandLens combines machine learning forecasting with
            price-response analysis to help retailers understand
            demand and evaluate revenue-maximizing pricing scenarios.
          </p>

          <div className="heroButtons">
            <a href="#pricing" className="primaryButton">
              Try Pricing Simulator →
            </a>

            <a href="#forecast" className="secondaryButton">
              Explore Model
            </a>
          </div>
        </div>

        <div className="heroCard">
          <div className="cardLabel">MODEL PERFORMANCE</div>

          <div className="bigMetric">19.95%</div>

          <div className="metricDescription">
            MAE improvement over 7-day baseline
          </div>

          <div className="miniMetrics">
            <div>
              <strong>1.069</strong>
              <span>MAE</span>
            </div>

            <div>
              <strong>2.235</strong>
              <span>RMSE</span>
            </div>

            <div>
              <strong>94.74%</strong>
              <span>WAPE</span>
            </div>
          </div>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="section" id="forecast">
        <div className="sectionHeading">
          <div>
            <div className="eyebrow">HOW IT WORKS</div>
            <h2>From historical sales to pricing decisions</h2>
          </div>

          <p>
            DemandLens turns historical retail data into forecasts
            and actionable pricing scenarios.
          </p>
        </div>

        <div className="pipeline">

          <div className="pipelineCard">
            <div className="number">01</div>
            <h3>Historical Data</h3>
            <p>
              Sales, prices, stores, products and calendar signals
              form the foundation of the model.
            </p>
            <div className="tag">Pandas</div>
          </div>

          <div className="arrow">→</div>

          <div className="pipelineCard">
            <div className="number">02</div>
            <h3>Feature Engineering</h3>
            <p>
              Lag features, rolling statistics, price changes and
              temporal signals capture demand patterns.
            </p>
            <div className="tag">Python + NumPy</div>
          </div>

          <div className="arrow">→</div>

          <div className="pipelineCard">
            <div className="number">03</div>
            <h3>Demand Forecast</h3>
            <p>
              A LightGBM regression model predicts expected product
              demand from the engineered features.
            </p>
            <div className="tag">LightGBM</div>
          </div>

          <div className="arrow">→</div>

          <div className="pipelineCard">
            <div className="number">04</div>
            <h3>Price Optimization</h3>
            <p>
              Demand response scenarios estimate how price changes
              could affect demand and revenue.
            </p>
            <div className="tag">Elasticity Model</div>
          </div>

        </div>
      </section>

      {/* MODEL SECTION */}
      <section className="section modelSection">
        <div className="sectionHeading">
          <div>
            <div className="eyebrow">MACHINE LEARNING</div>
            <h2>Demand forecasting engine</h2>
          </div>

          <p>
            The forecasting model learns from recent demand,
            seasonality, pricing and product/store characteristics.
          </p>
        </div>

        <div className="modelGrid">

          <div className="modelInfo">
            <div className="modelBadge">
              LIGHTGBM REGRESSOR
            </div>

            <h3>
              Gradient boosting for retail demand forecasting
            </h3>

            <p>
              DemandLens uses LightGBM to model nonlinear relationships
              between historical demand, pricing and calendar effects.
            </p>

            <div className="featureList">
              <div>
                <span>Rolling mean · 28 days</span>
                <strong>1,568</strong>
              </div>

              <div>
                <span>Rolling mean · 7 days</span>
                <strong>1,358</strong>
              </div>

              <div>
                <span>Rolling std · 7 days</span>
                <strong>918</strong>
              </div>

              <div>
                <span>Lag · 1 day</span>
                <strong>847</strong>
              </div>

              <div>
                <span>Lag · 7 days</span>
                <strong>829</strong>
              </div>
            </div>
          </div>

          <div className="performanceCard">

            <div className="performanceTitle">
              MODEL VS BASELINE
            </div>

            <div className="metricRow">
              <div>
                <span>7-day baseline</span>
                <strong>1.336</strong>
              </div>

              <div className="barContainer">
                <div
                  className="bar baseline"
                  style={{ width: "100%" }}
                />
              </div>
            </div>

            <div className="metricRow">
              <div>
                <span>LightGBM</span>
                <strong>1.069</strong>
              </div>

              <div className="barContainer">
                <div
                  className="bar model"
                  style={{ width: "80%" }}
                />
              </div>
            </div>

            <div className="improvementBox">
              <span>MAE improvement</span>
              <strong>19.95%</strong>
            </div>

          </div>
        </div>
      </section>

      {/* PRICING SIMULATOR */}
      <section className="section pricingSection" id="pricing">

        <div className="sectionHeading">
          <div>
            <div className="eyebrow">INTERACTIVE PRICING LAB</div>
            <h2>What price should you charge?</h2>
          </div>

          <p>
            Change the product assumptions and see how price,
            demand and revenue move under different elasticity
            assumptions.
          </p>
        </div>

        <div className="simulator">

          {/* CONTROLS */}
          <div className="controls">

            <div className="controlHeader">
              <span>SIMULATION INPUTS</span>
              <span className="liveBadge">LIVE</span>
            </div>

            <div className="controlGroup">
              <label>Current price</label>

              <div className="inputRow">
                <span>$</span>

                <input
                  type="number"
                  min="0.01"
                  step="0.01"
                  value={currentPrice}
                  onChange={(e) =>
                    setCurrentPrice(Number(e.target.value))
                  }
                />
              </div>
            </div>

            <div className="controlGroup">
              <label>Predicted demand</label>

              <div className="inputRow">
                <input
                  type="number"
                  min="0"
                  step="0.001"
                  value={baseDemand}
                  onChange={(e) =>
                    setBaseDemand(Number(e.target.value))
                  }
                />

                <span>units</span>
              </div>
            </div>

            <div className="controlGroup">

              <label>
                Price elasticity
                <span className="help">
                  ?
                </span>
              </label>

              <select
                value={elasticity}
                onChange={(e) =>
                  setElasticity(Number(e.target.value))
                }
              >
                <option value="-0.5">
                  -0.5 · Low sensitivity
                </option>

                <option value="-1">
                  -1.0 · Moderate sensitivity
                </option>

                <option value="-1.5">
                  -1.5 · High sensitivity
                </option>
              </select>
            </div>

            <div className="elasticityExplanation">
              <strong>
                Elasticity: {elasticity}
              </strong>

              <p>
                A 1% increase in price is estimated to change
                demand by approximately{" "}
                <strong>
                  {Math.abs(elasticity)}%
                </strong>{" "}
                in the opposite direction.
              </p>
            </div>

          </div>

          {/* RESULTS */}
          <div className="simulationResults">

            <div className="recommendation">

              <div>
                <div className="recommendationLabel">
                  RECOMMENDED SCENARIO
                </div>

                <h3>
                  {best.change > 0
                    ? `Increase price by ${best.change}%`
                    : best.change < 0
                    ? `Decrease price by ${Math.abs(best.change)}%`
                    : "Keep current price"}
                </h3>

                <p>
                  Highest estimated revenue under the selected
                  elasticity assumption.
                </p>
              </div>

              <div className="recommendationPrice">
                <span>Candidate price</span>
                <strong>
                  ${best.price.toFixed(2)}
                </strong>
              </div>

            </div>

            <div className="resultCards">

              <div className="resultCard">
                <span>EXPECTED DEMAND</span>
                <strong>
                  {best.demand.toFixed(2)}
                </strong>
                <small>units</small>
              </div>

              <div className="resultCard">
                <span>EXPECTED REVENUE</span>
                <strong>
                  ${best.revenue.toFixed(2)}
                </strong>
                <small>per period</small>
              </div>

              <div className="resultCard">
                <span>REVENUE VS CURRENT</span>
                <strong>
                  {revenueChange >= 0 ? "+" : ""}
                  {revenueChange.toFixed(1)}%
                </strong>
                <small>estimated</small>
              </div>

            </div>

            {/* REVENUE CHART */}
            <div className="chartCard">

              <div className="chartHeader">
                <div>
                  <strong>Revenue by price scenario</strong>
                  <span>
                    Estimated revenue response
                  </span>
                </div>

                <div className="chartLegend">
                  <span className="legendDot" />
                  Revenue
                </div>
              </div>

              <div className="chart">

                {results.map((item) => {

                  const height =
                    (item.revenue / maxRevenue) * 100;

                  const isBest =
                    item.change === best.change;

                  return (
                    <div
                      className="chartColumn"
                      key={item.change}
                    >

                      <div className="chartValue">
                        ${item.revenue.toFixed(2)}
                      </div>

                      <div className="chartBarWrapper">

                        <div
                          className={`chartBar ${
                            isBest ? "bestBar" : ""
                          }`}
                          style={{
                            height: `${height}%`,
                          }}
                        />

                      </div>

                      <span>
                        {item.change > 0
                          ? `+${item.change}%`
                          : `${item.change}%`}
                      </span>

                      <small>
                        ${item.price.toFixed(2)}
                      </small>

                    </div>
                  );
                })}

              </div>
            </div>

            {/* TABLE */}
            <div className="scenarioTable">

              <div className="tableHeader">
                <span>PRICE CHANGE</span>
                <span>PRICE</span>
                <span>DEMAND</span>
                <span>REVENUE</span>
              </div>

              {results.map((item) => (
                <div
                  className={`tableRow ${
                    item.change === best.change
                      ? "selectedRow"
                      : ""
                  }`}
                  key={item.change}
                >
                  <span>
                    {item.change > 0
                      ? `+${item.change}%`
                      : `${item.change}%`}
                  </span>

                  <span>
                    ${item.price.toFixed(2)}
                  </span>

                  <span>
                    {item.demand.toFixed(2)}
                  </span>

                  <span>
                    ${item.revenue.toFixed(2)}
                  </span>
                </div>
              ))}

            </div>

          </div>
        </div>

        <div className="disclaimer">
          <strong>Important:</strong> Pricing recommendations are
          scenario estimates based on historical observational
          relationships. They should not be interpreted as causal
          estimates or guarantees of future revenue.
        </div>

      </section>

      {/* TECHNOLOGY */}
      <section className="section techSection" id="methodology">

        <div className="sectionHeading">
          <div>
            <div className="eyebrow">TECHNOLOGY</div>
            <h2>Built as an end-to-end ML product</h2>
          </div>
        </div>

        <div className="techGrid">

          <div>
            <strong>Python</strong>
            <span>Data pipeline & modeling</span>
          </div>

          <div>
            <strong>Pandas</strong>
            <span>Data preparation</span>
          </div>

          <div>
            <strong>LightGBM</strong>
            <span>Demand forecasting</span>
          </div>

          <div>
            <strong>Scikit-learn</strong>
            <span>Evaluation & metrics</span>
          </div>

          <div>
            <strong>Next.js</strong>
            <span>Interactive web application</span>
          </div>

          <div>
            <strong>Vercel</strong>
            <span>Deployment</span>
          </div>

        </div>
      </section>

      {/* FOOTER */}
      <footer>
        <div>
          <strong>DemandLens</strong>
          <span>
            Retail demand forecasting & pricing intelligence
          </span>
        </div>

        <span>
          Built with Python · LightGBM · Next.js
        </span>
      </footer>

    </main>
  );
}