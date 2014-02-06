import FWCore.ParameterSet.Config as cms

import RecoTauTag.RecoTau.PFRecoTauChargedHadronBuilderPlugins_cfi as builders
import RecoTauTag.RecoTau.PFRecoTauChargedHadronQualityPlugins_cfi as ranking

from RecoTauTag.RecoTau.PFRecoTauQualityCuts_cfi import PFTauQualityCuts

ak4PFJetsRecoTauChargedHadrons = cms.EDProducer("PFRecoTauChargedHadronProducer",
    jetSrc = cms.InputTag("ak4PFJets"),
    jetRegionSrc = cms.InputTag("recoTauAK4PFJets08Region"),
    outputSelection = cms.string('pt > %1.1f' % PFTauQualityCuts.signalQualityCuts.minTrackPt.value()), # CV: apply minimum Pt cut as sanity check
    builders = cms.VPSet(
        builders.chargedPFCandidates,
        builders.tracks,
        builders.PFNeutralHadrons
    ),
    ranking = cms.VPSet(
        ranking.isChargedPFCandidate,
        ranking.isTrack,
        ranking.isPFNeutralHadron
    )
)
