ZC.LICENSE = ["569d52cefae586f634c54f86dc99e6a9", "b55b025e438fa8a98e32482b5f768ff5"];
let chartConfig = {
  type: "radar",
  plot: {
    aspect: "area",
    animation: {
      effect: 3,
      sequence: 1,
      speed: 700,
    },
  },
  scaleV: {
    visible: false,
  },
  scaleK: {
    values: "0:5:1",
    labels: ["STR", "VIT", "AGI", "LUX", "DEX", "INT"],
    guide: {
      alpha: 0.3,
      backgroundColor: "#c5c5c5 #718eb4",
      lineColor: "#607D8B",
      lineStyle: "solid",
    },
    item: {
      backgroundColor: "white",
      borderColor: "#aeaeae",
      borderRadius: "10px",
      borderWidth: "1px",
      fontColor: "#607D8B",
      padding: "5 10",
    },
    refLine: {
      lineColor: "#c10000",
    },
    tick: {
      lineColor: "#59869c",
      lineWidth: "2px",
      lineStyle: "dotted",
      size: 20,
    },
  },
  series: [
    {
      values: [60, 73, 85, 95, 65, 60],
      text: "farm",
    },
  ],
};

zingchart.render({
  id: "myChart",
  data: chartConfig,
  height: "100%",
  width: "100%",
});
