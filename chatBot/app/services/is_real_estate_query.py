


def is_real_estate_query(query:str):
    real_estate_keywords = [
    "real estate", "house", "property", "rent", "buy", "sell", "apartment", "mortgage","land","real estate", "property", "house", "rent", "apartment", "buy", "sell", "mortgage", "realtor",
    "real estate", "real estate near me", "real estate for sale", "real estate to buy", "real estate for rent",
    "real estate listings", "real estate agent", "real estate broker", "realtor", "real estate agency",
    "real estate companies", "residential real estate", "commercial real estate", "real estate market",
    "real estate trends", "real estate investment", "real estate investing", "real estate investment trusts",
    "real estate crowdfunding", "real estate development", "real estate finance", "real estate management",
    "real estate appraisal", "real estate marketing", "real estate software", "real estate websites",
    "real estate license", "real estate courses", "real estate education", "real estate blogs",
    "real estate photography", "real estate school", "real estate jobs", "real estate attorney",
    
    "homes for sale", "homes for sale near me", "houses for sale", "houses for sale near me",
    "apartments for sale", "land for sale", "luxury homes for sale", "cheap houses for sale",
    "new homes for sale", "vacation homes for sale", "mobile homes for sale", "condos for sale",
    "townhouses for sale", "studio flats under $1500", "buy a home", "buy a house", "buy real estate",
    "buy cheap apartments", "home buying process", "how to buy a house", "buy property online",
    "first-time home buyer", "first-time home buyer tips", "first-time home buyer guide",
    "first-time home buyer programs", "first-time buyer mortgage", "starter homes", "affordable homes for sale",
    "family-friendly apartments", "pet-friendly condo", "foreclosed homes for sale", "bank owned properties",
    "short sale homes", "bargain homes", "undervalued homes", "priced to sell",

    "how to sell a home", "sell your home", "sell a house", "sell my house fast", "selling a home",
    "selling your home", "home staging tips", "curb appeal tips", "home improvement tips", "home renovation ideas",
    "home selling process", "home selling checklist", "home selling fees", "pricing your home to sell",
    "negotiating home offers", "closing costs", "selling your home as-is", "prepare your home for sale",
    "selling real estate without a realtor", "real estate listing agent", "top real estate agents",
    "best real estate agent", "best real estate company", "real estate appraisal", "home appraisal",
    "home valuation", "home value estimator", "free home appraisal", "free home valuation",
    "free home valuation calculator", "home selling commission", "moving checklist",

    "homes for rent", "houses for rent", "apartments for rent", "home for rent", "house for rent",
    "apartment for rent", "rental properties", "rent to own homes", "rent to own homes near me",
    "property for rent", "apartments for rent in [city]", "rental property investment",

    "mortgage rates", "mortgage calculator", "home loans", "home equity loan", "home equity line of credit",
    "mortgage lenders", "mortgage lenders near me", "FHA loan", "FHA vs conventional loans", "FHA loans",
    "conventional mortgage", "reverse mortgage",

    "commercial real estate", "commercial property", "commercial property for sale",
    "commercial real estate near me", "office spaces for rent", "investment properties",
    "investment properties in [city]", "real estate investment strategies", "real estate investment opportunities",
    "real estate development near me", "real estate crowdfunding", "real estate investment trusts",
    "real estate finance", "commercial real estate for sale", "multi family homes for sale",
    "rental property investment", "real estate flipping trends", "real estate market forecast",

    "[city] real estate", "homes for sale in [city]", "houses for sale in [city]", "apartments for sale in [city]",
    "condos near [city]", "real estate agents in [city]", "real estate agency near me", "property for sale near me",
    "historic properties in [city]", "beachfront properties in [city]", "waterfront properties",
    "gated community homes", "suburban houses", "downtown apartments", "single-family homes", "townhouses in [town]",
    "townhomes for sale in [city/town]",

    "smart home technology", "eco-friendly homes", "sustainable homes", "energy-efficient homes in [city]",
    "virtual home tours", "3D home tours", "virtual open house", "smart home", "green building",
    "post-COVID real estate", "urban living trends", "suburban growth trends", "luxury real estate trends",
    "housing market trends", "housing market forecast", "luxury homes", "waterfront property",
    "country club homes", "golf course homes", "equestrian property", "historic properties", "homes with pools",
    "homes with large yards", "pet-friendly properties", "homes near schools", "retirement homes",
    "vacation homes", "mountain homes", "modern homes", "loft apartments", "open floor plan",
    "bar patio fireplace", "garage", "outdoor area", "airconditioning", "ensuite", "balcony", "shed", "study",
    "swimming pool", "water view", "granny flat", "studio", "dual living", "dual key", "tenant", "quiet enjoyment",
    "escrow", "closing", "tenancy", "trust deed", "zoning"
    ]

    return any(keyword in query.lower() for keyword in real_estate_keywords)
