func maxProfit(prices []int) int {
	maxProfit := 0
	buy,sell := 0,1
	for sell < len(prices) {
		if prices[sell] > prices[buy] {
			profit := prices[sell] - prices[buy]
			maxProfit = max(maxProfit, profit)
		} else {
			buy = sell
		}
		sell++
	}
	return maxProfit
}
