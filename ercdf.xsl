<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://itl.nist.gov/ns/voting/1500-100/v2 ../../schemas/nist-edf-v2_xmlschema.xsd"
    xmlns="http://itl.nist.gov/ns/voting/1500-100/v2" exclude-result-prefixes="xs" version="1.0">
    <xsl:output indent="yes"/>

    <xsl:template match="/">
        <ElectionReport xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://itl.nist.gov/ns/voting/1500-100/v2 ../NIST_V2_election_results_reporting.xsd"
            xmlns="http://itl.nist.gov/ns/voting/1500-100/v2">
            <xsl:apply-templates select="ElectionDefinition"/>
        </ElectionReport>
    </xsl:template>

    <xsl:template match="ElectionDefinition">
        <Election>
            <xsl:apply-templates select="BallotStyle"/>
            <xsl:apply-templates select="CandidateContest/Candidate"/>
            <xsl:apply-templates select="CandidateContest"/>
            <xsl:apply-templates select="BallotMeasureContest"/>
            
            <xsl:call-template name="ElectionScopeId" />
            <xsl:apply-templates select="Name" />
            <xsl:apply-templates select="StartDate"/>
            <xsl:apply-templates select="EndDate"/>
            <Type><xsl:value-of select="@type"/></Type>
        </Election>
        <Format>summary-contest</Format>
        <xsl:call-template name="GeneratedDate" />
        <xsl:apply-templates select="ReportingUnit"/>
        <xsl:apply-templates select="ReportingDevice"/>
        <xsl:call-template name="Headers"/>
        <Issuer>State</Issuer>
        <IssuerAbbreviation>US</IssuerAbbreviation>
        <xsl:apply-templates select="Party"/>
        <xsl:call-template name="Persons"/>
        <SequenceStart>1</SequenceStart>
        <SequenceEnd>1</SequenceEnd>
        <Status>pre-election</Status>
        <VendorApplicationId>ttv</VendorApplicationId>
    </xsl:template>

    <xsl:template match="BallotMeasureContest">
        <Contest xsi:type="BallotMeasureContest" ObjectId="{generate-id(.)}">
            <ElectionDistrictId>
                <xsl:value-of select="@scope"/>
            </ElectionDistrictId>
            <Name>
                <xsl:value-of select="description"/>
            </Name>
        </Contest>
    </xsl:template>

    <xsl:template match="BallotStyle">
        <BallotStyle>
            <GpUnitIds>
                <xsl:value-of select="GpUnitIds/@ids"/>
            </GpUnitIds>
            <xsl:apply-templates select="Section"/>
        </BallotStyle>
    </xsl:template>

    <xsl:template match="Candidate">
        <Candidate ObjectId="{@id}">
            <BallotName>
                <Text Language="en">
                    <xsl:value-of select="name"/>
                </Text>
            </BallotName>
        </Candidate>
    </xsl:template>

    <xsl:template match="CandidateContest">
        <Contest xsi:type="CandidateContest" ObjectId="{@id}">
            <xsl:for-each select="Candidate">
                <ContestSelection xsi:type="CandidateSelection"
                    ObjectId="{concat('contest-', generate-id(.))}">
                    <SequenceOrder>
                        <xsl:value-of select="position()"/>
                    </SequenceOrder>
                    <CandidateIds>
                        <xsl:value-of select="@id"/>
                    </CandidateIds>
                    <xsl:if test="@party">
                        <EndorsementPartyIds>
                            <xsl:value-of select="@party"/>
                        </EndorsementPartyIds>
                    </xsl:if>
                </ContestSelection>
            </xsl:for-each>
            <ElectionDistrictId>
                <xsl:value-of select="@scope"/>
            </ElectionDistrictId>
            <Name>
                <xsl:value-of select="@label"/>
            </Name>
            <xsl:apply-templates select="VoteVariation"/>
            <VotesAllowed>
                <xsl:value-of select="VotesAllowed"/>
            </VotesAllowed>
        </Contest>
    </xsl:template>

    <xsl:template match="EndDate">
        <EndDate>
            <xsl:value-of select="."/>
        </EndDate>
    </xsl:template>

    <xsl:template name="ElectionScopeId">
        <ElectionScopeId>
            <xsl:value-of select="@scope"/>
        </ElectionScopeId>
    </xsl:template>
    
    <xsl:template name="GeneratedDate">        
        <GeneratedDate>2018-01-29T00:00:00Z</GeneratedDate>
    </xsl:template>

    <xsl:template name="Headers">
        <xsl:for-each select="BallotStyle/Section/Header">
            <Header ObjectId="{generate-id(.)}">
                <Name>
                    <Text Language="en">
                        <xsl:value-of select="."/>
                    </Text>
                </Name>
            </Header>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="Name">
        <Name>
            <Text Language="en">
                <xsl:value-of select="."/>
            </Text>
        </Name>
    </xsl:template>

    <xsl:template match="Party">
        <Party ObjectId="{@id}">
            <Name>
                <Text Language="en">
                <xsl:value-of select="name"/>
                </Text>
            </Name>
        </Party>
    </xsl:template>

    <xsl:template name="Persons">
        <xsl:for-each select="CandidateContest/Candidate">
            <Person ObjectId="{generate-id(.)}">
                <FullName>
                    <Text Language="en">
                        <xsl:value-of select="name"/>
                    </Text>
                </FullName>
            </Person>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="ReportingDevice">
        <GpUnit xsi:type="ReportingDevice" ObjectId="{@id}">
            <DeviceClass>
                <Manufacturer>
                    <xsl:value-of select="DeviceClass/Manufacturer"/>
                </Manufacturer>
                <Model>
                    <xsl:value-of select="DeviceClass/Model"/>
                </Model>
                <Type>
                    <xsl:value-of select="DeviceClass/Type"/>
                </Type>
            </DeviceClass>
            <SerialNumber>
                <xsl:value-of select="SerialNumber"/>
            </SerialNumber>
        </GpUnit>
    </xsl:template>

    <xsl:template match="ReportingUnit">
        <GpUnit xsi:type="ReportingUnit" ObjectId="{@id}">
            <xsl:apply-templates select="Name"/>
            
            <Type>
                <xsl:value-of select="@type"/>
            </Type>
        </GpUnit>
    </xsl:template>

    <xsl:template match="Section">
        <OrderedContent xsi:type="OrderedHeader">
            <HeaderId>
                <xsl:value-of select="generate-id(Header)"/>
            </HeaderId>
            <OrderedContent xsi:type="OrderedContest">
                <xsl:for-each select="ContestIds/@ids">
                    <ContestId>
                        <xsl:value-of select="."/>
                    </ContestId>
                </xsl:for-each>
            </OrderedContent>
        </OrderedContent>
    </xsl:template>

    <xsl:template match="StartDate">
        <StartDate>
            <xsl:value-of select="."/>
        </StartDate>
    </xsl:template>

    

    <xsl:template match="VoteVariation">
        <VoteVariation>
            <xsl:value-of select="."/>
        </VoteVariation>
    </xsl:template>

</xsl:stylesheet>
