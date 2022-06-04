from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Jdbor:
    class Meta:
        name = "JDBOR"

    disorder_list: Optional["Jdbor.DisorderList"] = field(
        default=None,
        metadata={
            "name": "DisorderList",
            "type": "Element",
            "required": True,
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    copyright: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    dbserver: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class DisorderList:
        disorder: List["Jdbor.DisorderList.Disorder"] = field(
            default_factory=list,
            metadata={
                "name": "Disorder",
                "type": "Element",
                "min_occurs": 1,
            }
        )
        count: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

        @dataclass
        class Disorder:
            orpha_code: Optional[int] = field(
                default=None,
                metadata={
                    "name": "OrphaCode",
                    "type": "Element",
                    "required": True,
                }
            )
            expert_link: Optional["Jdbor.DisorderList.Disorder.ExpertLink"] = field(
                default=None,
                metadata={
                    "name": "ExpertLink",
                    "type": "Element",
                    "required": True,
                }
            )
            name: Optional["Jdbor.DisorderList.Disorder.Name"] = field(
                default=None,
                metadata={
                    "name": "Name",
                    "type": "Element",
                    "required": True,
                }
            )
            flag_value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "FlagValue",
                    "type": "Element",
                    "required": True,
                }
            )
            totalstatus: Optional["Jdbor.DisorderList.Disorder.Totalstatus"] = field(
                default=None,
                metadata={
                    "name": "Totalstatus",
                    "type": "Element",
                    "required": True,
                }
            )
            synonym_list: Optional["Jdbor.DisorderList.Disorder.SynonymList"] = field(
                default=None,
                metadata={
                    "name": "SynonymList",
                    "type": "Element",
                    "required": True,
                }
            )
            disorder_type: Optional["Jdbor.DisorderList.Disorder.DisorderType"] = field(
                default=None,
                metadata={
                    "name": "DisorderType",
                    "type": "Element",
                    "required": True,
                }
            )
            classification_level: Optional["Jdbor.DisorderList.Disorder.ClassificationLevel"] = field(
                default=None,
                metadata={
                    "name": "ClassificationLevel",
                    "type": "Element",
                    "required": True,
                }
            )
            disorder_disorder_association_list: Optional["Jdbor.DisorderList.Disorder.DisorderDisorderAssociationList"] = field(
                default=None,
                metadata={
                    "name": "DisorderDisorderAssociationList",
                    "type": "Element",
                    "required": True,
                }
            )
            summary_information_list: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList"] = field(
                default=None,
                metadata={
                    "name": "SummaryInformationList",
                    "type": "Element",
                    "required": True,
                }
            )
            aggregation_level_section: Optional["Jdbor.DisorderList.Disorder.AggregationLevelSection"] = field(
                default=None,
                metadata={
                    "name": "AggregationLevelSection",
                    "type": "Element",
                    "required": True,
                }
            )
            id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )

            @dataclass
            class ExpertLink:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    }
                )
                lang: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class Name:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    }
                )
                lang: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class Totalstatus:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    }
                )
                lang: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class SynonymList:
                synonym: List["Jdbor.DisorderList.Disorder.SynonymList.Synonym"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Synonym",
                        "type": "Element",
                    }
                )
                count: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

                @dataclass
                class Synonym:
                    value: str = field(
                        default="",
                        metadata={
                            "required": True,
                        }
                    )
                    lang: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "required": True,
                        }
                    )

            @dataclass
            class DisorderType:
                name: Optional["Jdbor.DisorderList.Disorder.DisorderType.Name"] = field(
                    default=None,
                    metadata={
                        "name": "Name",
                        "type": "Element",
                        "required": True,
                    }
                )
                id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

                @dataclass
                class Name:
                    value: str = field(
                        default="",
                        metadata={
                            "required": True,
                        }
                    )
                    lang: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "required": True,
                        }
                    )

            @dataclass
            class ClassificationLevel:
                name: Optional["Jdbor.DisorderList.Disorder.ClassificationLevel.Name"] = field(
                    default=None,
                    metadata={
                        "name": "Name",
                        "type": "Element",
                        "required": True,
                    }
                )
                id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

                @dataclass
                class Name:
                    value: str = field(
                        default="",
                        metadata={
                            "required": True,
                        }
                    )
                    lang: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "required": True,
                        }
                    )

            @dataclass
            class DisorderDisorderAssociationList:
                count: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class SummaryInformationList:
                summary_information: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation"] = field(
                    default=None,
                    metadata={
                        "name": "SummaryInformation",
                        "type": "Element",
                        "required": True,
                    }
                )
                count: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

                @dataclass
                class SummaryInformation:
                    text_section_list: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation.TextSectionList"] = field(
                        default=None,
                        metadata={
                            "name": "TextSectionList",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    text_auto: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation.TextAuto"] = field(
                        default=None,
                        metadata={
                            "name": "TextAuto",
                            "type": "Element",
                        }
                    )
                    id: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "required": True,
                        }
                    )
                    lang: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "required": True,
                        }
                    )

                    @dataclass
                    class TextSectionList:
                        text_section: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation.TextSectionList.TextSection"] = field(
                            default=None,
                            metadata={
                                "name": "TextSection",
                                "type": "Element",
                            }
                        )
                        count: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                                "required": True,
                            }
                        )

                        @dataclass
                        class TextSection:
                            text_section_type: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation.TextSectionList.TextSection.TextSectionType"] = field(
                                default=None,
                                metadata={
                                    "name": "TextSectionType",
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            contents: Optional[str] = field(
                                default=None,
                                metadata={
                                    "name": "Contents",
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                    "required": True,
                                }
                            )
                            lang: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                    "required": True,
                                }
                            )

                            @dataclass
                            class TextSectionType:
                                name: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation.TextSectionList.TextSection.TextSectionType.Name"] = field(
                                    default=None,
                                    metadata={
                                        "name": "Name",
                                        "type": "Element",
                                        "required": True,
                                    }
                                )
                                id: Optional[int] = field(
                                    default=None,
                                    metadata={
                                        "type": "Attribute",
                                        "required": True,
                                    }
                                )

                                @dataclass
                                class Name:
                                    value: str = field(
                                        default="",
                                        metadata={
                                            "required": True,
                                        }
                                    )
                                    lang: Optional[str] = field(
                                        default=None,
                                        metadata={
                                            "type": "Attribute",
                                            "required": True,
                                        }
                                    )

                    @dataclass
                    class TextAuto:
                        info: Optional["Jdbor.DisorderList.Disorder.SummaryInformationList.SummaryInformation.TextAuto.Info"] = field(
                            default=None,
                            metadata={
                                "name": "Info",
                                "type": "Element",
                                "required": True,
                            }
                        )

                        @dataclass
                        class Info:
                            value: str = field(
                                default="",
                                metadata={
                                    "required": True,
                                }
                            )
                            lang: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                    "required": True,
                                }
                            )

            @dataclass
            class AggregationLevelSection:
                aggregation_level_list: Optional["Jdbor.DisorderList.Disorder.AggregationLevelSection.AggregationLevelList"] = field(
                    default=None,
                    metadata={
                        "name": "AggregationLevelList",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass
                class AggregationLevelList:
                    aggregation_level: Optional["Jdbor.DisorderList.Disorder.AggregationLevelSection.AggregationLevelList.AggregationLevel"] = field(
                        default=None,
                        metadata={
                            "name": "AggregationLevel",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    count: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "required": True,
                        }
                    )

                    @dataclass
                    class AggregationLevel:
                        orpha_code: Optional[int] = field(
                            default=None,
                            metadata={
                                "name": "OrphaCode",
                                "type": "Element",
                                "required": True,
                            }
                        )
                        preferred_term: Optional["Jdbor.DisorderList.Disorder.AggregationLevelSection.AggregationLevelList.AggregationLevel.PreferredTerm"] = field(
                            default=None,
                            metadata={
                                "name": "PreferredTerm",
                                "type": "Element",
                                "required": True,
                            }
                        )
                        aggregation_level_status: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "AggregationLevelStatus",
                                "type": "Element",
                                "required": True,
                            }
                        )

                        @dataclass
                        class PreferredTerm:
                            value: str = field(
                                default="",
                                metadata={
                                    "required": True,
                                }
                            )
                            lang: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                    "required": True,
                                }
                            )
