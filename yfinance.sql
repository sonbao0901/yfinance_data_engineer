--create database
create database stock_db;




USE [stock_db]
GO
SET ANSI_NULLS ON     --return Unknown value instead of true, false when doing comparision
GO

SET QUOTED_IDENTIFIER ON --usefull for database that contains column's name containing space in it
GO
	
CREATE TABLE [dbo].[Stock](
	[SID] [int] IDENTITY(100,1) NOT NULL,
	[Ticker] [nvarchar](5) NOT NULL,
	[Exchange] [nvarchar](15) NULL,
	[Name] [nvarchar](100) NOT NULL,
	[DateTimePulled_EST] [nvarchar](100) NOT NULL,
	[Price] [decimal](18, 3) NULL,
	[Ask] [decimal](18, 3) NULL,
	[Bid] [decimal](18, 3) NULL,
	[DayLow] [decimal](18, 3) NULL,
	[DayHigh] [decimal](18, 3) NULL,
	[Volume] [decimal](38, 0) NULL,
	[MarketOpen] [decimal](18, 3) NULL,
	[MarketClose] [decimal](18, 3) NULL,
	[FiftyTwoWeekLow] [decimal](18, 3) NULL,
	[FiftyTwoWeekHigh] [decimal](18, 3) NULL,
	[FiftyDayAverage] [decimal](18, 3) NULL,
	[FiftyTwoWeekChange] [decimal](18, 2) NULL,
	[TwoHundredDayAverage] [decimal](18, 3) NULL,
	[AverageVolume] [decimal](38, 0) NULL,
	[TenDayAverageVolume] [decimal](38, 0) NULL,
	[Country] [nvarchar](4000) NULL,
	[Sector] [nvarchar](4000) NULL,
	[Industry] [nvarchar](4000) NULL,
	[LastDividendValue] [decimal](18, 2) NULL,
	[PayoutRatio] [decimal](38, 3) NULL,
	[ProfitMargins] [decimal](18, 3) NULL,
	[FloatShares] [decimal](38, 0) NULL,
	[ShortShares] [decimal](38, 0) NULL,
	[ShortSharesMonthAgo] [decimal](38, 0) NULL,
	[Employees] [decimal](38, 0) NULL,
	[BookValue] [decimal](18, 4) NULL,
	[EarningsQuarterlyGrowth] [decimal](18, 2) NULL,
	[NetIncomeToCommon] [decimal](18, 2) NULL,
	[SharesOutstanding] [decimal](38, 0) NULL,
	[ShortRatio] [decimal](18, 3) NULL,
	[Market] [nvarchar](4000) NULL,
	[LongBusinessSummary] [nvarchar](4000) NULL,
PRIMARY KEY CLUSTERED 
(
	[SID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO




USE [stock_db]
GO
SET ANSI_NULLS ON     --return Unknown value instead of true, false when doing comparision
GO
SET QUOTED_IDENTIFIER ON  --usefull for database that contains column's name containing space in it
GO

CREATE TABLE [dbo].[ASE](
	[ASE_ID] [int] NULL,
	[DateTimePulled_EST] [datetime] NULL,
	[Ticker] [nvarchar](5) NULL,
	[Price] [decimal](18, 3) NULL,
	[Ask] [decimal](18, 3) NULL,
	[Bid] [decimal](18, 3) NULL,
	[DayLow] [decimal](18, 3) NULL,
	[DayHigh] [decimal](18, 3) NULL,
	[MarketOpen] [decimal](18, 3) NULL,
	[MarketClose] [decimal](18, 3) NULL,
	[Volume] [decimal](18, 3) NULL
) ON [PRIMARY]
GO


select * from [dbo].[Stock];

TRUNCATE TABLE [dbo].[Stock]; --use to remove data from a table