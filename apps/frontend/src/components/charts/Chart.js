import React from "react";
import ReactEcharts from "echarts-for-react";

function Chart(props) {
  const { datasetOne, datasetTwo, metaData } = props;
  
  const getOption = () => {
    let values = [];
    let sets = [];

    Object.entries(datasetOne).forEach(entry => {
      sets = [...sets, entry[0]];
      entry[1].forEach(e => {
        values = [...new Set([...values, e.name])];
      });
    });

    let options = sets.map(set => {
      let obj = {};

      obj["series"] = [
        {
          stack: "group",
          data: datasetTwo[set]
        },
        {
          stack: "group",
          data: datasetOne[set]
        }
      ];

      obj["title"] = {
        text: `${metaData.title}, ${set}`
      };

      return obj;
    });

    return {
      baseOption: {
        timeline: {
          autoPlay: true,
          axisType: "category",
          bottom: 20,
          data: sets,
          height: null,
          inverse: true,
          left: null,
          orient: "vertical",
          playInterval: 1000,
          right: 0,
          top: 20,
          width: 55,
          label: {
            normal: {
              textStyle: {
                color: "#aaa"
              }
            },
            emphasis: {
              textStyle: {
                color: "#333"
              }
            }
          },
          symbol: "none",
          lineStyle: {
            color: "#aaa"
          },
          checkpointStyle: {
            color: "#354EF6",
            borderColor: "transparent",
            borderWidth: 2
          },
          controlStyle: {
            showNextBtn: false,
            showPrevBtn: false,
            normal: {
              color: "#354EF6",
              borderColor: "#354EF6"
            },
            emphasis: {
              color: "#5d71f7",
              borderColor: "#5d71f7"
            }
          }
        },
        color: ["#e91e63", "#354EF6"],
        title: {
          subtext: metaData.subtext,
          textAlign: "left",
          left: "5%"
        },
        tooltip: { backgroundColor: "#555", borderWidth: 0, padding: 10 },
        legend: {
          data: metaData.legend,
          itemGap: 35,
          itemHeight: 18,
          right: "11%",
          top: 20
        },
        calculable: true,
        grid: {
          top: 100,
          bottom: 150,
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "shadow",
              label: {
                show: true,
                formatter: function(params) {
                  return params.value.replace("\n", "");
                }
              }
            }
          }
        },
        xAxis: [
          {
            axisLabel: {
              interval: 0,
              rotate: 55,
              textStyle: {
                baseline: "top",
                color: "#333",
                fontSize: 10,
                fontWeight: "bold"
              }
            },
            axisLine: { lineStyle: { color: "#aaa" }, show: true },
            axisTick: { show: false },
            name: metaData.x,
            data: values,
            splitLine: { show: false },
            type: "category"
          }
        ],
        yAxis: [
          {
            axisLabel: {
              textStyle: { fontSize: 10 }
            },
            axisLine: { show: false },
            axisTick: { show: false },
            name: metaData.y,
            splitLine: {
              lineStyle: {
                type: "dotted"
              }
            },
            type: "value"
          }
        ],
        series: metaData.series
      },
      options: options
    };
  };

    return (
      <ReactEcharts
        option={getOption()}
        style={{ height: "80vh", left: 50, top: 50, width: "90vw" }}
        opts={{ renderer: "svg" }}
      />
    );
}

export default Chart